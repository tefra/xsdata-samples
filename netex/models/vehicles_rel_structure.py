from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle import Vehicle
from .vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicles_RelStructure"

    vehicle_ref_or_vehicle: List[Union[VehicleRef, Vehicle]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleRef",
                    "type": VehicleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Vehicle",
                    "type": Vehicle,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
