from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .route_link import RouteLink

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteLinksInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "routeLinksInFrame_RelStructure"

    route_link: Sequence[RouteLink] = field(
        default_factory=list,
        metadata={
            "name": "RouteLink",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
