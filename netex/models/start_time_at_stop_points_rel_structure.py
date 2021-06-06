from dataclasses import dataclass, field
from typing import List
from .start_time_at_stop_point import StartTimeAtStopPoint
from .start_time_at_stop_point_ref import StartTimeAtStopPointRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StartTimeAtStopPointsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "startTimeAtStopPoints_RelStructure"

    start_time_at_stop_point_ref: List[StartTimeAtStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "StartTimeAtStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time_at_stop_point: List[StartTimeAtStopPoint] = field(
        default_factory=list,
        metadata={
            "name": "StartTimeAtStopPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
