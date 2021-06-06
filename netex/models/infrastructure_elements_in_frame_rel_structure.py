from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .railway_element import RailwayElement
from .road_element import RoadElement
from .wire_element import WireElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureElementsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "infrastructureElementsInFrame_RelStructure"

    railway_element: List[RailwayElement] = field(
        default_factory=list,
        metadata={
            "name": "RailwayElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_element: List[RoadElement] = field(
        default_factory=list,
        metadata={
            "name": "RoadElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_element: List[WireElement] = field(
        default_factory=list,
        metadata={
            "name": "WireElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
