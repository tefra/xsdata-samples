from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .estimated_passing_time import EstimatedPassingTime
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "estimatedPassingTimes_RelStructure"

    estimated_passing_time: Sequence[EstimatedPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
