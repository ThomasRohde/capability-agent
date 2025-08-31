from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme

from .io_utils import read_json_file, write_json_file
from .models import validate_model


app = typer.Typer(help="Business Capability Model manipulation utilities.")
console = Console(theme=Theme({"error": "bold red", "info": "cyan", "success": "bold green"}))


@app.command()
def reset(
    input: Path = typer.Option(..., exists=True, dir_okay=False, readable=True, help="Input model JSON path"),
    output: Optional[Path] = typer.Option(None, dir_okay=False, help="Output JSON path (optional, defaults to input)"),
    in_place: bool = typer.Option(False, "--in-place", help="Modify input file directly"),
):
    """Reset all 'capability' attributes to 0 in the model."""
    console.print(Panel.fit("bcm-wrench: Resetting capability attributes", title="reset"))

    # Determine output path
    if in_place and output:
        console.print("Cannot use both --in-place and --output options", style="error")
        raise typer.Exit(1)
    
    output_path = input if in_place else (output or input)

    try:
        data = read_json_file(input)
        model = validate_model(data)
    except Exception as e:
        console.print(f"Input model validation failed: {e}", style="error")
        raise typer.Exit(1)

    # Reset capability attribute to 0 for all nodes
    reset_count = 0
    for capability in model.root:
        if hasattr(capability, 'capability') and getattr(capability, 'capability', None) != 0:
            reset_count += 1
        # Set capability to 0 using setattr to handle extra fields
        setattr(capability, 'capability', 0)

    try:
        write_json_file(output_path, [c.model_dump() for c in model.root])
    except Exception as e:
        console.print(f"Failed to write output: {e}", style="error")
        raise typer.Exit(1)

    console.print(f"Reset {reset_count} capabilities -> {output_path}", style="success")


@app.command()
def slice(
    input: Path = typer.Option(..., exists=True, dir_okay=False, readable=True, help="Input model JSON path"),
    capability_name: str = typer.Option(..., "--capability-name", help="Name of the capability to extract subtree from"),
    output: Path = typer.Option(..., dir_okay=False, help="Output JSON path for the slice"),
):
    """Extract a subtree from a named capability and output to a new file."""
    console.print(Panel.fit("bcm-wrench: Extracting capability subtree", title="slice"))

    try:
        data = read_json_file(input)
        model = validate_model(data)
    except Exception as e:
        console.print(f"Input model validation failed: {e}", style="error")
        raise typer.Exit(1)

    # Find the capability by name
    target_capability = None
    for capability in model.root:
        if capability.name == capability_name:
            target_capability = capability
            break

    if not target_capability:
        console.print(f"Capability '{capability_name}' not found in model", style="error")
        raise typer.Exit(1)

    # Extract subtree starting from target capability
    try:
        subtree = model.extract_subtree(target_capability.id)
    except Exception as e:
        console.print(f"Failed to extract subtree: {e}", style="error")
        raise typer.Exit(1)

    try:
        write_json_file(output, [c.model_dump() for c in subtree.root])
    except Exception as e:
        console.print(f"Failed to write output: {e}", style="error")
        raise typer.Exit(1)

    console.print(f"Extracted {len(subtree.root)} nodes from '{capability_name}' -> {output}", style="success")


def main() -> None:
    app()


if __name__ == "__main__":
    main()