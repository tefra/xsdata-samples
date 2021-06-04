from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.railway_junction import RailwayJunction
from netex.models.road_junction import RoadJunction
from netex.models.wire_junction import WireJunction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureJunctionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "infrastructureJunctionsInFrame_RelStructure"

    railway_junction: List[RailwayJunction] = field(
        default_factory=list,
        metadata={
            "name": "RailwayJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_junction: List[RoadJunction] = field(
        default_factory=list,
        metadata={
            "name": "RoadJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wire_junction: List[WireJunction] = field(
        default_factory=list,
        metadata={
            "name": "WireJunction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
