"""Capability Agent package."""

from .cli import main
from .models import Capability, CapabilityList, validate_model
from .io_utils import ContextOptions, read_json_file, write_json_file, load_system_message, parse_context_level
from .service import augment_model

__all__ = [
    "main",
    "Capability",
    "CapabilityList",
    "validate_model",
    "ContextOptions",
    "read_json_file",
    "write_json_file",
    "load_system_message",
    "parse_context_level",
    "augment_model",
]
__all__.extend(["__version__"])

__version__ = "0.1.0"
