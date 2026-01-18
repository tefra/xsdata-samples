from __future__ import annotations

from dataclasses import dataclass

from .relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FrameContainmentStructure(RelationshipStructure):
    class Meta:
        name = "frameContainmentStructure"
