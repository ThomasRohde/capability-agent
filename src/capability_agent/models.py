from __future__ import annotations

import uuid
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, RootModel, ValidationError, field_validator


class Capability(BaseModel):
    id: str
    name: str
    description: str
    parent: Optional[str] = None

    class Config:
        extra = "allow"

    @field_validator("id")
    @classmethod
    def validate_uuid4(cls, v: str) -> str:
        try:
            u = uuid.UUID(v)
        except Exception as e:  # noqa: BLE001
            raise ValueError(f"Invalid UUID: {v}") from e
        if u.version != 4:
            raise ValueError("id must be UUID4")
        return v


class CapabilityList(RootModel[List[Capability]]):
    def by_id(self) -> Dict[str, Capability]:
        return {c.id: c for c in self.root}

    def children_map(self) -> Dict[str, List[Capability]]:
        m: Dict[str, List[Capability]] = {}
        for c in self.root:
            if c.parent is not None:
                m.setdefault(c.parent, []).append(c)
        return m

    def roots(self) -> List[Capability]:
        return [c for c in self.root if c.parent is None]

    def leaves(self) -> List[Capability]:
        children = self.children_map()
        return [c for c in self.root if len(children.get(c.id, [])) == 0]

    def leaves_for_generation(self) -> List[Capability]:
        """Return leaf nodes that need generation (capability attribute is 0 or missing)."""
        children = self.children_map()
        leaves = [c for c in self.root if len(children.get(c.id, [])) == 0]
        
        # Filter leaves that need generation (capability is 0, missing, or -1 for error retry)
        return [
            leaf for leaf in leaves 
            if getattr(leaf, 'capability', 0) <= 0  # Include 0 (unprocessed) and -1 (error)
        ]

    def extract_subtree(self, root_id: str) -> "CapabilityList":
        """Extract a subtree starting from the given root capability ID."""
        by_id = self.by_id()
        children = self.children_map()
        
        if root_id not in by_id:
            raise ValueError(f"Capability with id '{root_id}' not found")
        
        # Collect all descendants recursively
        result = []
        
        def collect_descendants(node_id: str) -> None:
            if node_id in by_id:
                result.append(by_id[node_id])
                for child in children.get(node_id, []):
                    collect_descendants(child.id)
        
        collect_descendants(root_id)
        
        # Set the root node's parent to null since it's now the root of the subtree
        if result:
            result[0] = result[0].model_copy(update={"parent": None})
        
        return CapabilityList.model_validate(result)

    @field_validator("root")
    @classmethod
    def validate_unique_ids(cls, v: List[Capability]) -> List[Capability]:
        seen = set()
        for c in v:
            if c.id in seen:
                raise ValueError(f"Duplicate id detected: {c.id}")
            seen.add(c.id)
        return v


def validate_model(data: Any) -> CapabilityList:
    """Parse and validate a raw JSON array of capabilities.

    - Ensures UUID4 ids (via field validator)
    - Ensures unique ids (via root validator)
    - Ensures parent references (if present) exist in the set of ids
    """
    try:
        lst = CapabilityList.model_validate(data)
    except ValidationError as e:  # re-raise for callers to present nicely
        raise e

    ids = {c.id for c in lst.root}
    for c in lst.root:
        if c.parent is not None and c.parent not in ids:
            raise ValueError(f"Node '{c.name}' has missing parent id: {c.parent}")
    return lst

