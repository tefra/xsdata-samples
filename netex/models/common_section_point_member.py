from dataclasses import dataclass
from netex.models.point_on_section_versioned_child_structure import PointOnSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonSectionPointMember(PointOnSectionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
