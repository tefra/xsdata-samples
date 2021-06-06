from dataclasses import dataclass
from .point_on_link_versioned_child_structure import PointOnLinkVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLink(PointOnLinkVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
