from dataclasses import dataclass, field
from typing import List
from netex.models.journey_pattern_run_time import JourneyPatternRunTime
from netex.models.journey_pattern_run_time_ref import JourneyPatternRunTimeRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternRunTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "journeyPatternRunTimes_RelStructure"

    journey_pattern_run_time_ref: List[JourneyPatternRunTimeRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternRunTimeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_run_time: List[JourneyPatternRunTime] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
