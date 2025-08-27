from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.theme import Theme

from .io_utils import (
    ContextFormat,
    load_system_message,
    parse_context_level,
    read_json_file,
    write_json_file,
)
from .models import validate_model
from .service import augment_model


app = typer.Typer(help="Augment a business capability model by generating sub-capabilities for each leaf.")
console = Console(theme=Theme({"error": "bold red", "info": "cyan"}))


@app.command()
def run(
    input: Path = typer.Option(..., exists=True, dir_okay=False, readable=True, help="Input model JSON path"),
    template: Path = typer.Option(..., exists=True, dir_okay=False, readable=True, help="Jinja2 template path"),
    output: Path = typer.Option(..., dir_okay=False, writable=True, help="Output JSON path"),
    max_capabilities: int = typer.Option(5, min=1, max=50, help="Max sub-capabilities per leaf"),
    tasks: int = typer.Option(4, min=1, help="Number of concurrent LLM calls"),
    override_system_message: Optional[Path] = typer.Option(None, exists=True, dir_okay=False, readable=True, help="Optional system message file"),
    context_level: Optional[str] = typer.Option(None, help="Comma-separated context: full_tree,parent,siblings"),
    context_format: str = typer.Option("markdown", help="Context format: json, markdown, or xml"),
    log_prompts: Optional[Path] = typer.Option(
        None,
        "--log-prompts",
        help="Directory to write rendered prompts (one file per leaf).",
        exists=False,
        file_okay=False,
        dir_okay=True,
        writable=True,
    ),
    streaming: bool = typer.Option(False, "--streaming", help="Use streaming API for real-time progress (requires --tasks 1)"),
    restart: bool = typer.Option(False, "--restart", help="Resume generation from input file, ignoring output option"),
):
    """Augment INPUT model and write enhanced OUTPUT as JSON array."""
    console.print(Panel.fit("business-capgen: Augmenting capability model", title="capability-agent"))

    try:
        data = read_json_file(input)
        model = validate_model(data)
    except Exception as e:  # noqa: BLE001
        console.print(f"Input model validation failed: {e}", style="error")
        raise typer.Exit(1)

    try:
        ctx_opts = parse_context_level(context_level)
    except ValueError as e:
        console.print(str(e), style="error")
        raise typer.Exit(1)

    try:
        ctx_format = ContextFormat(context_format.lower())
    except ValueError:
        console.print(f"Invalid context format: {context_format}. Must be one of: json, markdown, xml", style="error")
        raise typer.Exit(1)

    try:
        system_message = load_system_message(override_system_message)
    except Exception as e:  # noqa: BLE001
        console.print(f"Failed to load system message: {e}", style="error")
        raise typer.Exit(1)

    # Resolve log prompts directory
    log_dir: Optional[Path] = log_prompts

    # Validate streaming configuration
    if streaming and tasks > 1:
        console.print("Warning: Streaming requires --tasks 1. Setting tasks=1 automatically.", style="info")
        tasks = 1

    # Determine output path - use input path if restart mode
    output_path = input if restart else output
    
    if restart:
        console.print(f"Restart mode: will update {input} in-place", style="info")

    try:
        enhanced, usage_stats = augment_model(
            model=model,
            template_path=template,
            context_opts=ctx_opts,
            context_format=ctx_format,
            system_message=system_message,
            max_capabilities=max_capabilities,
            tasks=tasks,
            log_prompts_dir=log_dir,
            use_streaming=streaming,
            restart_mode=restart,
            input_path=input if restart else None,
        )
    except Exception as e:  # noqa: BLE001
        import traceback
        console.print(f"Augmentation failed: {e}", style="error")
        console.print("Full traceback:", style="error")
        console.print(traceback.format_exc(), style="error")
        raise typer.Exit(1)

    # Emit as plain list of dicts
    try:
        write_json_file(output_path, [c.model_dump() for c in enhanced.root])
    except Exception as e:  # noqa: BLE001
        console.print(f"Failed to write output: {e}", style="error")
        raise typer.Exit(1)
    console.print(f"Wrote {len(enhanced.root)} nodes -> {output_path}", style="info")
    
    # Display usage statistics summary
    if usage_stats.total_tokens > 0:
        usage_table = Table(title="📊 Usage Statistics")
        usage_table.add_column("Metric", style="cyan")
        usage_table.add_column("Value", style="green")
        
        # Basic information
        usage_table.add_row("Model", usage_stats.model_name)
        usage_table.add_row("Total Tokens", f"{usage_stats.total_tokens:,}")
        
        # Input token breakdown
        usage_table.add_row("", "")  # Separator
        usage_table.add_row("Input Tokens", f"{usage_stats.input_tokens:,}")
        
        if usage_stats.has_caching:
            usage_table.add_row("  └─ Cached Tokens", f"{usage_stats.cached_tokens:,}")
            usage_table.add_row("  └─ Non-cached Tokens", f"{usage_stats.non_cached_input_tokens:,}")
            usage_table.add_row("  └─ Cache Hit Rate", f"{usage_stats.cache_hit_rate:.1f}%")
        else:
            usage_table.add_row("  └─ All New Tokens", f"{usage_stats.input_tokens:,}")
            
        # Output token breakdown  
        usage_table.add_row("", "")  # Separator
        usage_table.add_row("Output Tokens", f"{usage_stats.output_tokens:,}")
        
        if usage_stats.has_reasoning:
            usage_table.add_row("  └─ Reasoning Tokens", f"{usage_stats.reasoning_tokens:,}")
            regular_tokens = usage_stats.output_tokens - usage_stats.reasoning_tokens
            usage_table.add_row("  └─ Regular Tokens", f"{regular_tokens:,}")
        
        console.print()
        console.print(usage_table)
        
        # Show cost savings information if caching was used
        if usage_stats.has_caching:
            console.print(f"💡 [bold green]Cost savings:[/bold green] You saved ~50% on {usage_stats.cached_tokens:,} cached tokens!", style="info")


def main() -> None:
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
