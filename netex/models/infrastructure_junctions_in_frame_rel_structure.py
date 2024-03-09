from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .railway_junction import RailwayJunction
from .road_junction import RoadJunction
from .wire_junction import WireJunction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureJunctionsInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "infrastructureJunctionsInFrame_RelStructure"

    railway_junction_or_road_junction_or_wire_junction: List[
        Union[RailwayJunction, RoadJunction, WireJunction]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RailwayJunction",
                    "type": RailwayJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadJunction",
                    "type": RoadJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireJunction",
                    "type": WireJunction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
