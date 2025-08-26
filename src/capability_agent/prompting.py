from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .io_utils import ContextFormat, ContextOptions
from .models import Capability, CapabilityList


def serialize_capability_minimal(cap: Capability, by_id: Dict[str, Capability]) -> Dict[str, Any]:
    """Serialize capability with only essential fields: name, description, parent name."""
    result = {
        "name": cap.name,
        "description": cap.description,
    }
    if cap.parent and cap.parent in by_id:
        result["parent"] = by_id[cap.parent].name
    return result


def format_capabilities_as_json(capabilities: List[Dict[str, Any]]) -> str:
    """Format capabilities as clean JSON."""
    return json.dumps(capabilities, ensure_ascii=False, indent=2)


def format_capabilities_as_markdown(capabilities: List[Dict[str, Any]]) -> str:
    """Format capabilities as Markdown list."""
    if not capabilities:
        return ""
    
    lines = []
    for cap in capabilities:
        lines.append(f"### {cap['name']}")
        lines.append(f"{cap['description']}")
        if "parent" in cap:
            lines.append(f"**Parent:** {cap['parent']}")
        lines.append("")  # Empty line between capabilities
    
    return "\n".join(lines).rstrip()


def format_capabilities_as_xml(capabilities: List[Dict[str, Any]]) -> str:
    """Format capabilities as XML."""
    if not capabilities:
        return "<capabilities></capabilities>"
    
    lines = ["<capabilities>"]
    for cap in capabilities:
        lines.append("  <capability>")
        lines.append(f"    <name>{cap['name']}</name>")
        lines.append(f"    <description>{cap['description']}</description>")
        if "parent" in cap:
            lines.append(f"    <parent>{cap['parent']}</parent>")
        lines.append("  </capability>")
    lines.append("</capabilities>")
    
    return "\n".join(lines)


def build_prompt_context(model: CapabilityList, node: Capability, ctx: ContextOptions, format: ContextFormat = ContextFormat.MARKDOWN) -> Dict[str, Any]:
    by_id = {c.id: c for c in model.root}
    children: Dict[str, List[Capability]] = {}
    for c in model.root:
        if c.parent is not None:
            children.setdefault(c.parent, []).append(c)

    # Format function mapping
    format_func = {
        ContextFormat.JSON: format_capabilities_as_json,
        ContextFormat.MARKDOWN: format_capabilities_as_markdown,
        ContextFormat.XML: format_capabilities_as_xml,
    }[format]

    # Build context with pre-formatted strings
    context: Dict[str, Any] = {"node": node}
    
    # Add formatted current capability
    current_capability_minimal = [serialize_capability_minimal(node, by_id)]
    context["formatted_capability"] = format_func(current_capability_minimal)
    
    # Add formatted context sections
    if ctx.parent and node.parent:
        parent_cap = by_id[node.parent]
        parent_minimal = [serialize_capability_minimal(parent_cap, by_id)]
        context["parent"] = parent_cap
        context["formatted_parent"] = format_func(parent_minimal)
    else:
        context["formatted_parent"] = format_func([])
        
    if ctx.siblings:
        if node.parent and node.parent in children:
            sibling_caps = [c for c in children[node.parent] if c.id != node.id]
            siblings_minimal = [serialize_capability_minimal(c, by_id) for c in sibling_caps]
            context["siblings"] = sibling_caps
            context["formatted_siblings"] = format_func(siblings_minimal)
        else:
            context["siblings"] = []
            context["formatted_siblings"] = format_func([])
    else:
        context["formatted_siblings"] = format_func([])
        
    if ctx.full_tree:
        full_tree_minimal = [serialize_capability_minimal(c, by_id) for c in model.root]
        context["full_tree"] = model.root
        context["formatted_full_tree"] = format_func(full_tree_minimal)
    else:
        context["formatted_full_tree"] = format_func([])
        
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
