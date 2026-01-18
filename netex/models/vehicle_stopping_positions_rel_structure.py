from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_stopping_position import VehicleStoppingPosition
from .vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPositionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleStoppingPositions_RelStructure"

    vehicle_stopping_position_ref_or_vehicle_stopping_position: Iterable[
        VehicleStoppingPositionRef | VehicleStoppingPosition
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleStoppingPositionRef",
                    "type": VehicleStoppingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPosition",
                    "type": VehicleStoppingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
