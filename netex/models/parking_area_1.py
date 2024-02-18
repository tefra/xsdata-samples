from dataclasses import dataclass
from .parking_area_version_structure import ParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingArea1(ParkingAreaVersionStructure):
    class Meta:
        name = "ParkingArea"
        namespace = "http://www.netex.org.uk/netex"
