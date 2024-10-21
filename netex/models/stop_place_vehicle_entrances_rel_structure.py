from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from .vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceVehicleEntrancesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopPlaceVehicleEntrances_RelStructure"

    vehicle_entrance_ref_or_stop_place_vehicle_entrance: Iterable[
        Union[VehicleEntranceRef, StopPlaceVehicleEntrance]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleEntranceRef",
                    "type": VehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceVehicleEntrance",
                    "type": StopPlaceVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
