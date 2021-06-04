from dataclasses import dataclass
from netex.models.point_on_link_ref_structure_2 import PointOnLinkRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnLinkRef(PointOnLinkRefStructure2):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
