from dataclasses import dataclass

from .point_on_link_ref_structure_1 import PointOnLinkRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLinkRef(PointOnLinkRefStructure1):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
