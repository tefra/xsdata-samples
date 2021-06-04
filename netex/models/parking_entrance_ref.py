from dataclasses import dataclass
from netex.models.parking_entrance_ref_structure import ParkingEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingEntranceRef(ParkingEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
