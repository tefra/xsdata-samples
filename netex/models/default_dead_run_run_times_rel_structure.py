from dataclasses import dataclass, field
from typing import List

from .default_dead_run_run_time import DefaultDeadRunRunTime
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultDeadRunRunTimesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "defaultDeadRunRunTimes_RelStructure"

    default_dead_run_run_time: List[DefaultDeadRunRunTime] = field(
        default_factory=list,
        metadata={
            "name": "DefaultDeadRunRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
