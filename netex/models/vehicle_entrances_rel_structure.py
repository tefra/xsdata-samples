from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.vehicle_entrance import VehicleEntrance
from netex.models.vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEntrancesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleEntrances_RelStructure"

    vehicle_entrance_ref: List[VehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_entrance: List[VehicleEntrance] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntrance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
