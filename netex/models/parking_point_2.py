from dataclasses import dataclass
from netex.models.parking_point_version_structure import ParkingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPoint2(ParkingPointVersionStructure):
    class Meta:
        name = "ParkingPoint"
        namespace = "http://www.netex.org.uk/netex"
