from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_element import TrainElement
from .vehicle import Vehicle

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehiclesInFrame_RelStructure"

    train_element: List[TrainElement] = field(
        default_factory=list,
        metadata={
            "name": "TrainElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "Vehicle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
