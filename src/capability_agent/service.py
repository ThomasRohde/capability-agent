from __future__ import annotations

import uuid
from pathlib import Path
from typing import List

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

from .io_utils import ContextOptions
from .llm import call_openai, ensure_client
from .models import Capability, CapabilityList
from .prompting import build_prompt_context, render_prompt


console = Console(theme=Theme({"error": "bold red", "info": "cyan"}))


def augment_model(
    model: CapabilityList,
    template_path: Path,
    context_opts: ContextOptions,
    system_message: str,
    max_capabilities: int,
) -> CapabilityList:
    client = ensure_client()

    leaves = model.leaves()
    new_nodes: List[Capability] = []

    # Rich progress with a single overall bar (one tick per generation/leaf)
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

        for leaf in leaves:
            # Optionally show which leaf is being processed in the description
            progress.update(overall_task, description=f"Generating: {leaf.name}")

            # Build prompt context and render
            context = build_prompt_context(model, leaf, context_opts)
            context["max_capabilities"] = max_capabilities
            user_prompt = render_prompt(template_path, context)

            # Call LLM (one generation per leaf)
            generated = call_openai(client, system_message, user_prompt, max_capabilities)

            # Inherit extra fields from parent (leaf) except reserved keys
            inherited = leaf.model_dump()
            inherited.pop("id", None)
            inherited.pop("name", None)
            inherited.pop("description", None)

            for item in generated:
                node_data = {
                    **inherited,
                    "id": str(uuid.uuid4()),
                    "name": item["name"],
                    "description": item["description"],
                    "parent": leaf.id,
                }
                new_nodes.append(Capability.model_validate(node_data))

            # Advance the overall bar once per generation/leaf
            progress.advance(overall_task, 1)

    output = CapabilityList.model_validate([*model.root, *new_nodes])

    # Re-validate uniqueness
    seen: set[str] = set()
    for c in output.root:
        if c.id in seen:
            raise ValueError(f"Duplicate id detected in output: {c.id}")
        seen.add(c.id)
    return output
