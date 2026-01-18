from __future__ import annotations

from dataclasses import dataclass

from .entity_structure import EntityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Entity(EntityStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
