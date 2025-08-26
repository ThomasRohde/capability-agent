from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme

from .io_utils import (
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

    try:
        enhanced = augment_model(
            model=model,
            template_path=template,
            context_opts=ctx_opts,
            system_message=system_message,
            max_capabilities=max_capabilities,
            tasks=tasks,
            log_prompts_dir=log_dir,
            use_streaming=streaming,
        )
    except Exception as e:  # noqa: BLE001
        console.print(f"Augmentation failed: {e}", style="error")
        raise typer.Exit(1)

    # Emit as plain list of dicts
    try:
        write_json_file(output, [c.model_dump() for c in enhanced.root])
    except Exception as e:  # noqa: BLE001
        console.print(f"Failed to write output: {e}", style="error")
        raise typer.Exit(1)
    console.print(f"Wrote {len(enhanced.root)} nodes -> {output}", style="info")


def main() -> None:
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
