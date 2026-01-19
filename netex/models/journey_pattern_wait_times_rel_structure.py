from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .journey_pattern_wait_time import JourneyPatternWaitTime
from .journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternWaitTimesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "journeyPatternWaitTimes_RelStructure"

    journey_pattern_wait_time_ref_or_journey_pattern_wait_time: Sequence[
        JourneyPatternWaitTimeRef | JourneyPatternWaitTime
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPatternWaitTimeRef",
                    "type": JourneyPatternWaitTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternWaitTime",
                    "type": JourneyPatternWaitTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
