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

    route_ref: List[RouteRef] = field(
        default_factory=list,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route: List[Route1] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
