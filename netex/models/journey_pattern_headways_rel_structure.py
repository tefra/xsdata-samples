from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .journey_pattern_headway import JourneyPatternHeadway
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternHeadwaysRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "journeyPatternHeadways_RelStructure"

    journey_pattern_headway: Iterable[JourneyPatternHeadway] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
