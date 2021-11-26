from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_route import FlexibleRoute
from .route_1 import Route1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routesInFrame_RelStructure"

    flexible_route: List[FlexibleRoute] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleRoute",
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
