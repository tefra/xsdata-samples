from dataclasses import dataclass, field
from typing import List

from .journey_pattern_headway import JourneyPatternHeadway
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyPatternHeadwaysRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "journeyPatternHeadways_RelStructure"

    journey_pattern_headway: List[JourneyPatternHeadway] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
