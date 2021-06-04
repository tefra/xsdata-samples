from dataclasses import dataclass
from netex.models.parking_point_version_structure import ParkingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GaragePointVersionStructure(ParkingPointVersionStructure):
    class Meta:
        name = "GaragePoint_VersionStructure"
