from __future__ import annotations

import uuid
from pathlib import Path
from typing import List, Sequence, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeElapsedColumn,
)
from rich.theme import Theme

from .io_utils import ContextFormat, ContextOptions, ensure_dir, safe_filename, timestamp_for_filename, save_progress
from .llm import call_openai, call_openai_streaming, ensure_client, UsageStats
from .models import Capability, CapabilityList
from .prompting import build_prompt_context, render_prompt


console = Console(theme=Theme({"error": "bold red", "info": "cyan"}))


def augment_model(
    model: CapabilityList,
    template_path: Path,
    context_opts: ContextOptions,
    context_format: ContextFormat,
    system_message: str,
    max_capabilities: int,
    tasks: int = 4,
    log_prompts_dir: Optional[Path] = None,
    use_streaming: bool = False,
    restart_mode: bool = False,
    input_path: Optional[Path] = None,
    openai_log_dir: Optional[Path] = None,
    openai_log_level: str = "none",
) -> tuple[CapabilityList, UsageStats]:
    client = ensure_client(openai_log_dir, openai_log_level)
    total_usage = UsageStats()  # Initialize usage tracking

    # Use different leaf selection based on restart mode
    if restart_mode:
        leaves = model.leaves_for_generation()
        if not leaves:
            console.print("No capabilities need generation. All leaves already generated.", style="info")
            return model, total_usage
    else:
        leaves = model.leaves()
    
    new_nodes: List[Capability] = []
    progress_lock = threading.Lock()  # Thread-safe progress saving
    
    def save_leaf_progress(leaf: Capability) -> None:
        """Mark a leaf as generated and save progress if in restart mode."""
        if restart_mode and input_path:
            with progress_lock:  # Ensure thread-safe progress saving
                # Update the capability attribute for the processed leaf
                leaf_dict = leaf.model_dump()
                leaf_dict['capability'] = 1
                # Clear any previous error marker on success
                leaf_dict.pop('error', None)
                
                # Find and update the leaf in the current model
                for i, c in enumerate(model.root):
                    if c.id == leaf.id:
                        # Create updated capability and replace in model
                        updated_cap = Capability.model_validate(leaf_dict)
                        model.root[i] = updated_cap
                        break
                
                # Save progress
                current_data = [c.model_dump() for c in model.root] + [c.model_dump() for c in new_nodes]
                save_progress(input_path, current_data)

    def generate_children(leaf: Capability) -> tuple[Sequence[Capability], UsageStats]:
        try:
            # Build prompt context and render
            context = build_prompt_context(model, leaf, context_opts, context_format)
            context["max_capabilities"] = max_capabilities
            user_prompt = render_prompt(template_path, context)

            # Optionally log the rendered prompt per leaf
            if log_prompts_dir is not None:
                try:
                    ensure_dir(log_prompts_dir)
                    stem = f"{timestamp_for_filename()}_{safe_filename(leaf.name)}"
                    # include short id to avoid collisions
                    short_id = (leaf.id or "")[:8]
                    if short_id:
                        stem = f"{stem}_{short_id}"
                    out_path = (log_prompts_dir / f"{stem}.prompt.txt").resolve()
                    out_path.write_text(user_prompt, encoding="utf-8")
                except Exception as e:  # noqa: BLE001
                    # Do not fail augmentation if logging fails; surface as info
                    console.print(f"Prompt log failed for {leaf.name}: {e}", style="error")

            # Call LLM (one generation per leaf)
            if use_streaming and tasks <= 1:  # Only use streaming in serial mode
                generated, usage_stats = call_openai_streaming(
                    client, system_message, user_prompt, max_capabilities, 
                    show_progress=True, leaf_name=leaf.name
                )
            else:
                generated, usage_stats = call_openai(
                    client, system_message, user_prompt, max_capabilities
                )

            # Inherit extra fields from parent (leaf) except reserved keys
            inherited = leaf.model_dump()
            # Remove reserved and internal fields so they don't propagate to children
            for key in ("id", "name", "description", "capability", "error"):
                inherited.pop(key, None)

            children: List[Capability] = []
            for item in generated:
                node_data = {
                    **inherited,
                    "id": str(uuid.uuid4()),
                    "name": item["name"],
                    "description": item["description"],
                    "parent": leaf.id,
                    "capability": 1,  # Mark new nodes as generated
                }
                children.append(Capability.model_validate(node_data))
            
            # Save progress after successful generation
            save_leaf_progress(leaf)
            return children, usage_stats
            
        except Exception as e:
            # Enhanced error logging with leaf context
            error_msg = f"Failed to generate children for leaf '{leaf.name}' (ID: {leaf.id}): {str(e)}"
            console.print(f"[error]{error_msg}[/error]")
            
            # Mark this leaf as having encountered an error in restart mode
            if restart_mode and input_path:
                with progress_lock:
                    try:
                        # Mark leaf with error state rather than completed
                        leaf_dict = leaf.model_dump()
                        leaf_dict['capability'] = -1  # Use -1 to indicate error state
                        leaf_dict['error'] = str(e)  # Store error message
                        
                        # Find and update the leaf in the current model
                        for i, c in enumerate(model.root):
                            if c.id == leaf.id:
                                updated_cap = Capability.model_validate(leaf_dict)
                                model.root[i] = updated_cap
                                break
                        
                        # Save progress with error state
                        current_data = [c.model_dump() for c in model.root] + [c.model_dump() for c in new_nodes]
                        save_progress(input_path, current_data)
                    except Exception as save_error:
                        console.print(f"[error]Failed to save error state: {save_error}[/error]")
            
            # Re-raise the original exception
            raise e

    # Handle streaming vs concurrent execution differently
    if use_streaming and tasks <= 1:
        # Serial execution with streaming - no outer progress bar to avoid conflicts
        console.print(f"[info]Streaming generation for {len(leaves)} leaves...[/info]")
        for i, leaf in enumerate(leaves, 1):
            console.print(f"[info]Processing leaf {i}/{len(leaves)}: {leaf.name}[/info]")
            children, usage = generate_children(leaf)
            new_nodes.extend(children)
            total_usage += usage
    else:
        # Concurrent execution or non-streaming - use overall progress bar
        if restart_mode:
            console.print(f"[info]Restart mode: processing {len(leaves)} remaining leaves with {tasks} workers...[/info]")
        
        with Progress(
            SpinnerColumn(style="info"),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=console,
            transient=True,
        ) as progress:
            task_description = "Generating sub-capabilities (restart mode)" if restart_mode else "Generating sub-capabilities"
            overall_task = progress.add_task(task_description, total=len(leaves))

            if tasks <= 1 or len(leaves) <= 1:
                for leaf in leaves:
                    progress.update(overall_task, description=f"Generating: {leaf.name}")
                    children, usage = generate_children(leaf)
                    new_nodes.extend(children)
                    total_usage += usage
                    progress.advance(overall_task, 1)
            else:
                progress.update(overall_task, description=f"Generating with {tasks} workers…")
                with ThreadPoolExecutor(max_workers=tasks) as executor:
                    future_map = {executor.submit(generate_children, leaf): leaf for leaf in leaves}
                    # Track which leaves failed for better error reporting
                    failed_leaves: List[tuple[Capability, Exception]] = []
                    successful_count = 0
                    
                    for fut in as_completed(future_map):
                        leaf = future_map[fut]
                        try:
                            children, usage = fut.result()
                            new_nodes.extend(children)
                            total_usage += usage
                            successful_count += 1
                        except Exception as e:  # noqa: BLE001
                            failed_leaves.append((leaf, e))
                            console.print(f"[error]Error processing leaf '{leaf.name}': {str(e)}[/error]")
                        finally:
                            progress.advance(overall_task, 1)
                    
                    # If we have failures, provide detailed information
                    if failed_leaves:
                        error_summary = []
                        for leaf, exc in failed_leaves:
                            error_summary.append(f"  - {leaf.name} (ID: {leaf.id}): {str(exc)}")
                        
                        failure_msg = (
                            f"\n{len(failed_leaves)} out of {len(leaves)} leaves failed to process:\n" +
                            "\n".join(error_summary) +
                            f"\n\nSuccessfully processed: {successful_count}/{len(leaves)} leaves."
                        )
                        
                        if restart_mode:
                            failure_msg += (
                                "\n\nIn restart mode: progress has been saved for successful leaves. "
                                "You can re-run with --restart to continue processing the failed leaves."
                            )
                        
                        # For now, still fail fast, but with much better error information
                        raise Exception(f"Augmentation failed with detailed errors:{failure_msg}")

    output = CapabilityList.model_validate([*model.root, *new_nodes])

    # Re-validate uniqueness and integrity
    seen: set[str] = set()
    for c in output.root:
        if c.id in seen:
            raise ValueError(f"Duplicate id detected in output: {c.id}")
        seen.add(c.id)
    
    # In restart mode, verify we haven't lost any data
    if restart_mode:
        original_count = len(model.root)
        final_count = len(output.root)
        added_count = len(new_nodes)
        
        console.print(
            f"[info]Restart summary: {original_count} original + {added_count} new = {final_count} total capabilities[/info]"
        )
        
        # Sanity check: ensure we didn't lose any original capabilities
        if final_count < original_count:
            raise ValueError(
                f"Data integrity error: final count ({final_count}) is less than original count ({original_count}). "
                "This suggests data loss during processing."
            )
    
    return output, total_usage
