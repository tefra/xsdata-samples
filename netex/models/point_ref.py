from dataclasses import dataclass
from netex.models.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointRef(PointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
