from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .traffic_control_point import TrafficControlPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrafficControlPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trafficControlPointsInFrame_RelStructure"

    traffic_control_point: Iterable[TrafficControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "TrafficControlPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
