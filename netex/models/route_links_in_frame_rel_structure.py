from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .route_link import RouteLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routeLinksInFrame_RelStructure"

    route_link: Iterable[RouteLink] = field(
        default_factory=list,
        metadata={
            "name": "RouteLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
