from dataclasses import dataclass
from netex.models.parking_version_structure import ParkingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Parking(ParkingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
