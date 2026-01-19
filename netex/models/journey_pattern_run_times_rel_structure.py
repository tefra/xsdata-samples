from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .journey_pattern_run_time import JourneyPatternRunTime
from .journey_pattern_run_time_ref import JourneyPatternRunTimeRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternRunTimesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "journeyPatternRunTimes_RelStructure"

    journey_pattern_run_time_ref_or_journey_pattern_run_time: Sequence[
        JourneyPatternRunTimeRef | JourneyPatternRunTime
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPatternRunTimeRef",
                    "type": JourneyPatternRunTimeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRunTime",
                    "type": JourneyPatternRunTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
