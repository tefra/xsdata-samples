from dataclasses import dataclass
from .point_on_line_section_versioned_child_structure import (
    PointOnLineSectionVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLineSection(PointOnLineSectionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
