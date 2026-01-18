from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .timing_point_in_journey_pattern import TimingPointInJourneyPattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimingPointsInJourneyPatternRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "timingPointsInJourneyPattern_RelStructure"

    timing_point_in_journey_pattern: Iterable[TimingPointInJourneyPattern] = (
        field(
            default_factory=list,
            metadata={
                "name": "TimingPointInJourneyPattern",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 2,
            },
        )
    )
