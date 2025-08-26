from __future__ import annotations

import uuid
from pathlib import Path
from typing import List, Sequence, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

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

from .io_utils import ContextOptions, ensure_dir, safe_filename, timestamp_for_filename
from .llm import call_openai, call_openai_streaming, ensure_client
from .models import Capability, CapabilityList
from .prompting import build_prompt_context, render_prompt


console = Console(theme=Theme({"error": "bold red", "info": "cyan"}))


def augment_model(
    model: CapabilityList,
    template_path: Path,
    context_opts: ContextOptions,
    system_message: str,
    max_capabilities: int,
    tasks: int = 4,
    log_prompts_dir: Optional[Path] = None,
    use_streaming: bool = False,
) -> CapabilityList:
    client = ensure_client()

    leaves = model.leaves()
    new_nodes: List[Capability] = []

    def generate_children(leaf: Capability) -> Sequence[Capability]:
        # Build prompt context and render
        context = build_prompt_context(model, leaf, context_opts)
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
            generated = call_openai_streaming(
                client, system_message, user_prompt, max_capabilities, 
                show_progress=True, leaf_name=leaf.name
            )
        else:
            generated = call_openai(
                client, system_message, user_prompt, max_capabilities
            )

        # Inherit extra fields from parent (leaf) except reserved keys
        inherited = leaf.model_dump()
        inherited.pop("id", None)
        inherited.pop("name", None)
        inherited.pop("description", None)

        children: List[Capability] = []
        for item in generated:
            node_data = {
                **inherited,
                "id": str(uuid.uuid4()),
                "name": item["name"],
                "description": item["description"],
                "parent": leaf.id,
            }
            children.append(Capability.model_validate(node_data))
        return children

    # Handle streaming vs concurrent execution differently
    if use_streaming and tasks <= 1:
        # Serial execution with streaming - no outer progress bar to avoid conflicts
        console.print(f"[info]Streaming generation for {len(leaves)} leaves...[/info]")
        for i, leaf in enumerate(leaves, 1):
            console.print(f"[info]Processing leaf {i}/{len(leaves)}: {leaf.name}[/info]")
            new_nodes.extend(generate_children(leaf))
    else:
        # Concurrent execution or non-streaming - use overall progress bar
        with Progress(
            SpinnerColumn(style="info"),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            console=console,
            transient=True,
        ) as progress:
            overall_task = progress.add_task(
                "Generating sub-capabilities", total=len(leaves)
            )

            if tasks <= 1 or len(leaves) <= 1:
                for leaf in leaves:
                    progress.update(overall_task, description=f"Generating: {leaf.name}")
                    new_nodes.extend(generate_children(leaf))
                    progress.advance(overall_task, 1)
            else:
                progress.update(overall_task, description=f"Generating with {tasks} workers…")
                with ThreadPoolExecutor(max_workers=tasks) as executor:
                    future_map = {executor.submit(generate_children, leaf): leaf for leaf in leaves}
                    for fut in as_completed(future_map):
                        leaf = future_map[fut]
                        try:
                            children = fut.result()
                            new_nodes.extend(children)
                        except Exception as e:  # noqa: BLE001
                            # Fail fast on any leaf error
                            raise e
                        finally:
                            progress.advance(overall_task, 1)

    output = CapabilityList.model_validate([*model.root, *new_nodes])

    # Re-validate uniqueness
    seen: set[str] = set()
    for c in output.root:
        if c.id in seen:
            raise ValueError(f"Duplicate id detected in output: {c.id}")
        seen.add(c.id)
    return output
