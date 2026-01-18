from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .routing_constraint_zone import RoutingConstraintZone

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutingConstraintZonesInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "routingConstraintZonesInFrame_RelStructure"

    routing_constraint_zone: Iterable[RoutingConstraintZone] = field(
        default_factory=list,
        metadata={
            "name": "RoutingConstraintZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
