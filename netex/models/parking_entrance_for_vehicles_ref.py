from dataclasses import dataclass
from netex.models.parking_entrance_for_vehicles_ref_structure import ParkingEntranceForVehiclesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingEntranceForVehiclesRef(ParkingEntranceForVehiclesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
