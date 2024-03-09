from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_route import FlexibleRoute
from .route_1 import Route1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routesInFrame_RelStructure"

    route: List[Union[FlexibleRoute, Route1]] = field(
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
                    "type": Route1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
