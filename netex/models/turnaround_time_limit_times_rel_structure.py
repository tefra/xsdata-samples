from collections.abc import Iterable
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .turnaround_time_limit_time import TurnaroundTimeLimitTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TurnaroundTimeLimitTimesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "turnaroundTimeLimitTimes_RelStructure"

    turnaround_time_limit_time: Iterable[TurnaroundTimeLimitTime] = field(
        default_factory=list,
        metadata={
            "name": "TurnaroundTimeLimitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
