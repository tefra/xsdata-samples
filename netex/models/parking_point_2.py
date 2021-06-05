from dataclasses import dataclass
from netex.models.relief_point_version_structure import ReliefPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPoint2(ReliefPointVersionStructure):
    class Meta:
        name = "ParkingPoint_"
        namespace = "http://www.netex.org.uk/netex"
