from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_element import TrainElement
from .vehicle import Vehicle

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehiclesInFrame_RelStructure"

    train_element_or_vehicle: Iterable[TrainElement | Vehicle] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainElement",
                    "type": TrainElement,
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
