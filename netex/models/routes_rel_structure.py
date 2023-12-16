from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .route import Route
from .route_ref import RouteRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routes_RelStructure"

    route_ref_or_route: List[Union[RouteRef, Route]] = field(
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
                    "type": Route,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
