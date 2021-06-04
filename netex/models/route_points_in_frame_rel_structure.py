from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.route_point import RoutePoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutePointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routePointsInFrame_RelStructure"

    route_point: List[RoutePoint] = field(
        default_factory=list,
        metadata={
            "name": "RoutePoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
