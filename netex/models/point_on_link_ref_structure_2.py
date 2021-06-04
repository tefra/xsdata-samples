from dataclasses import dataclass
from netex.models.point_on_link_ref_structure_1 import PointOnLinkRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLinkRefStructure2(PointOnLinkRefStructure1):
    class Meta:
        name = "PointOnLinkRefStructure"
