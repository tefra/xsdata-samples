from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .target_passing_time import TargetPassingTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TargetPassingTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "targetPassingTimes_RelStructure"

    target_passing_time: Sequence[TargetPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "TargetPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
