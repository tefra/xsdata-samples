from dataclasses import dataclass, field
from typing import List
from .point_in_journey_pattern import PointInJourneyPattern
from .stop_point_in_journey_pattern import StopPointInJourneyPattern
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .timing_point_in_journey_pattern import TimingPointInJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointsInJourneyPatternRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pointsInJourneyPattern_RelStructure"

    point_in_journey_pattern: List[PointInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "PointInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
    stop_point_in_journey_pattern: List[StopPointInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "StopPointInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
    timing_point_in_journey_pattern: List[TimingPointInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "TimingPointInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
