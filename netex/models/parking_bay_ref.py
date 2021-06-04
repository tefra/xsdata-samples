from dataclasses import dataclass
from netex.models.parking_bay_ref_structure import ParkingBayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBayRef(ParkingBayRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
