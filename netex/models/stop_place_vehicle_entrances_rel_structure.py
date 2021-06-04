from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from netex.models.vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceVehicleEntrancesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopPlaceVehicleEntrances_RelStructure"

    vehicle_entrance_ref: List[VehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_vehicle_entrance: List[StopPlaceVehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceVehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
