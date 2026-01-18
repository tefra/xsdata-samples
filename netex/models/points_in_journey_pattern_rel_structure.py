from collections.abc import Iterable
from dataclasses import dataclass, field

from .point_in_journey_pattern import PointInJourneyPattern
from .stop_point_in_journey_pattern import StopPointInJourneyPattern
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .timing_point_in_journey_pattern import TimingPointInJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointsInJourneyPatternRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "pointsInJourneyPattern_RelStructure"

    point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern: Iterable[
        PointInJourneyPattern
        | StopPointInJourneyPattern
        | TimingPointInJourneyPattern
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointInJourneyPattern",
                    "type": PointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPattern",
                    "type": StopPointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPattern",
                    "type": TimingPointInJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "min_occurs": 2,
        },
    )
