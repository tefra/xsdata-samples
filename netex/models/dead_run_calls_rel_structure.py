from dataclasses import dataclass, field
from typing import List
from netex.models.dead_run_call_versioned_child_structure import DeadRunCallVersionedChildStructure
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeadRunCallsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "deadRunCalls_RelStructure"

    dead_run_call: List[DeadRunCallVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunCall",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 2,
        }
    )
