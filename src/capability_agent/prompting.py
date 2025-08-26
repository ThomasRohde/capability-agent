from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .io_utils import ContextOptions
from .models import Capability, CapabilityList


def build_prompt_context(model: CapabilityList, node: Capability, ctx: ContextOptions) -> Dict[str, Any]:
    by_id = {c.id: c for c in model.root}
    children: Dict[str, List[Capability]] = {}
    for c in model.root:
        if c.parent is not None:
            children.setdefault(c.parent, []).append(c)

    def serialize(cap: Capability) -> Dict[str, Any]:
        return cap.model_dump()

    context: Dict[str, Any] = {"node": serialize(node)}
    if ctx.parent and node.parent:
        context["parent"] = serialize(by_id[node.parent])
    if ctx.siblings:
        if node.parent and node.parent in children:
            context["siblings"] = [serialize(c) for c in children[node.parent] if c.id != node.id]
        else:
            context["siblings"] = []
    if ctx.full_tree:
        context["full_tree"] = [serialize(c) for c in model.root]
    return context


def render_prompt(template_path: Path, context: Dict[str, Any]) -> str:
    env = Environment(
        loader=FileSystemLoader(template_path.parent),
        undefined=StrictUndefined,
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(template_path.name)
    return template.render(**context)
