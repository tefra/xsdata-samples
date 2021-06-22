from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_entrance import VehicleEntrance
from .vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEntrancesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleEntrances_RelStructure"

    vehicle_entrance_ref_or_vehicle_entrance: List[object] = field(
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
                    "name": "VehicleEntrance",
                    "type": VehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
