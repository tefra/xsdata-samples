from dataclasses import dataclass, field
from typing import List
from .previous_call import PreviousCall
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PreviousCallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "previousCalls_RelStructure"

    previous_call: List[PreviousCall] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
