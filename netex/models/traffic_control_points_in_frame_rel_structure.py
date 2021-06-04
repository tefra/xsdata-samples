from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.traffic_control_point import TrafficControlPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrafficControlPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trafficControlPointsInFrame_RelStructure"

    traffic_control_point: List[TrafficControlPoint] = field(
        default_factory=list,
        metadata={
            "name": "TrafficControlPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
