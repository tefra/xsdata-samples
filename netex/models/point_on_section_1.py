from dataclasses import dataclass
from .point_on_section_versioned_child_structure import PointOnSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnSection1(PointOnSectionVersionedChildStructure):
    class Meta:
        name = "PointOnSection"
        namespace = "http://www.netex.org.uk/netex"