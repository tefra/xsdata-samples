from dataclasses import dataclass, field
from typing import List
from .onward_call import OnwardCall
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnwardCallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "onwardCalls_RelStructure"

    onward_call: List[OnwardCall] = field(
        default_factory=list,
        metadata={
            "name": "OnwardCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
