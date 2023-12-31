from dataclasses import dataclass
from .parking_area_version_structure import ParkingAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiParkingAreaVersionStructure(ParkingAreaVersionStructure):
    class Meta:
        name = "TaxiParkingArea_VersionStructure"
