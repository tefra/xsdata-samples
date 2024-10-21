from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_entrance_for_vehicles import ParkingEntranceForVehicles
from .parking_entrance_for_vehicles_ref import ParkingEntranceForVehiclesRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingEntrancesForVehiclesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingEntrancesForVehicles_RelStructure"

    parking_entrance_for_vehicles_ref_or_parking_entrance_for_vehicles: Iterable[
        Union[ParkingEntranceForVehiclesRef, ParkingEntranceForVehicles]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingEntranceForVehiclesRef",
                    "type": ParkingEntranceForVehiclesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingEntranceForVehicles",
                    "type": ParkingEntranceForVehicles,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
