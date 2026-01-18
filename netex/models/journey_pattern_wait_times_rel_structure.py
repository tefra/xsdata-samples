from collections.abc import Iterable
from dataclasses import dataclass, field

from .journey_pattern_wait_time import JourneyPatternWaitTime
from .journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternWaitTimesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "journeyPatternWaitTimes_RelStructure"

    journey_pattern_wait_time_ref_or_journey_pattern_wait_time: Iterable[
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
