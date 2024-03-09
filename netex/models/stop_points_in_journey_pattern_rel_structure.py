from dataclasses import dataclass, field
from typing import List

from .stop_point_in_journey_pattern import StopPointInJourneyPattern
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPointsInJourneyPatternRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "stopPointsInJourneyPattern_RelStructure"

    stop_point_in_journey_pattern: List[StopPointInJourneyPattern] = field(
        default_factory=list,
        metadata={
            "name": "StopPointInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        },
    )
