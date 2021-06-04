from dataclasses import dataclass
from netex.models.parking_ref_structure import ParkingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingRef(ParkingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
