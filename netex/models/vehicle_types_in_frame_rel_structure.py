from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .compound_train import CompoundTrain
from .containment_aggregation_structure import ContainmentAggregationStructure
from .simple_vehicle_type import SimpleVehicleType
from .train import Train
from .vehicle_type import VehicleType

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleTypesInFrame_RelStructure"

    choice: Iterable[
        CompoundTrain | Train | VehicleType | SimpleVehicleType
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrain",
                    "type": CompoundTrain,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Train",
                    "type": Train,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleType",
                    "type": VehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SimpleVehicleType",
                    "type": SimpleVehicleType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
