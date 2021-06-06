from dataclasses import dataclass, field
from typing import List
from .journey_pattern_wait_time import JourneyPatternWaitTime
from .journey_pattern_wait_time_ref import JourneyPatternWaitTimeRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternWaitTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "journeyPatternWaitTimes_RelStructure"

    journey_pattern_wait_time_ref: List[JourneyPatternWaitTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternWaitTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_wait_time: List[JourneyPatternWaitTime] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
