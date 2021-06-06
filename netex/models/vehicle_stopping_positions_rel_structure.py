from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_stopping_position import VehicleStoppingPosition
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPositionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleStoppingPositions_RelStructure"

    vehicle_stopping_position_ref: List[VehicleStoppingPositionRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPositionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_position: List[VehicleStoppingPosition] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
