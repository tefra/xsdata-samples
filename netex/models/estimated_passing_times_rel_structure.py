from dataclasses import dataclass, field
from typing import List

from .estimated_passing_time import EstimatedPassingTime
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EstimatedPassingTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "estimatedPassingTimes_RelStructure"

    estimated_passing_time: List[EstimatedPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
