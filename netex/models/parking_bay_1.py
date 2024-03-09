from dataclasses import dataclass

from .parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBay1(ParkingBayVersionStructure):
    class Meta:
        name = "ParkingBay"
        namespace = "http://www.netex.org.uk/netex"
