from dataclasses import dataclass
from netex.models.parking_capacity_ref_structure import ParkingCapacityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingCapacityRef(ParkingCapacityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
