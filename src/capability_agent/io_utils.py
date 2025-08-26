from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from rich.console import Console
from rich.theme import Theme


console = Console(theme=Theme({"error": "bold red", "info": "cyan"}))


class ContextFormat(Enum):
    JSON = "json"
    MARKDOWN = "markdown"
    XML = "xml"


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


def ensure_dir(path: Path) -> None:
    """Create directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


_FILENAME_SAFE_RE = re.compile(r"[^A-Za-z0-9._-]+")


def safe_filename(name: str, max_len: int = 80) -> str:
    """Return a filesystem-safe, reasonably short filename stem.

    - Lowercases
    - Replaces unsafe chars with '-'
    - Collapses repeats and trims to max_len
    """
    stem = name.strip().lower()
    stem = stem.replace(" ", "-")
    stem = _FILENAME_SAFE_RE.sub("-", stem)
    stem = re.sub(r"-+", "-", stem).strip("-._")
    if len(stem) > max_len:
        stem = stem[:max_len].rstrip("-._")
    return stem or "capability"


def timestamp_for_filename() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def save_progress(path: Path, model_data: List[Dict[str, Any]]) -> None:
    """Atomically save progress to the input file."""
    # Write to temporary file first, then rename for atomicity
    temp_path = path.with_suffix(path.suffix + ".tmp")
    try:
        write_json_file(temp_path, model_data)
        temp_path.replace(path)
    except Exception:
        # Clean up temp file if something went wrong
        if temp_path.exists():
            temp_path.unlink()
        raise
