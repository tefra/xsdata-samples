from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_route import FlexibleRoute
from .route import Route

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routesInFrame_RelStructure"

    flexible_route_or_route: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleRoute",
                    "type": FlexibleRoute,
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
