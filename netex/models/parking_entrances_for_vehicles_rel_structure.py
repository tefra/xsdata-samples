from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_entrance_for_vehicles import ParkingEntranceForVehicles
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingEntrancesForVehiclesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingEntrancesForVehicles_RelStructure"

    parking_entrance_for_vehicles_ref: List[ParkingEntranceForVehiclesRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehiclesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_entrance_for_vehicles: List[ParkingEntranceForVehicles] = field(
        default_factory=list,
        metadata={
            "name": "ParkingEntranceForVehicles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
