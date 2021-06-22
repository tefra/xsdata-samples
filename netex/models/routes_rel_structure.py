from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .route_1 import Route1
from .route_ref import RouteRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routes_RelStructure"

    route_ref_or_route: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RouteRef",
                    "type": RouteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Route",
                    "type": Route1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
