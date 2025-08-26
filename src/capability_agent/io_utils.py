from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from rich.console import Console
from rich.theme import Theme


console = Console(theme=Theme({"error": "bold red", "info": "cyan"}))


@dataclass
class ContextOptions:
    full_tree: bool = False
    parent: bool = False
    siblings: bool = False


def read_json_file(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json_file(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_system_message(path: Optional[Path]) -> str:
    default = (
        "You are an expert enterprise architect. Generate concise, useful sub-capabilities as JSON."
    )
    if not path:
        return default
    return path.read_text(encoding="utf-8")


def parse_context_level(value: Optional[str]) -> ContextOptions:
    opts = ContextOptions()
    if not value:
        return opts
    for part in value.split(","):
        p = part.strip().lower()
        if p == "full_tree":
            opts.full_tree = True
        elif p == "parent":
            opts.parent = True
        elif p == "siblings":
            opts.siblings = True
        elif p == "":
            continue
        else:
            raise ValueError(f"Unknown context level option: {p}")
    return opts
