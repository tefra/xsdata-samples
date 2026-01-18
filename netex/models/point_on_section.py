from __future__ import annotations

from dataclasses import dataclass

from .point_on_section_versioned_child_structure import (
    PointOnSectionVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnSection(PointOnSectionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
