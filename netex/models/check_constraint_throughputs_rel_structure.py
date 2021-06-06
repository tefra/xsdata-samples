from dataclasses import dataclass, field
from typing import List
from .check_constraint_throughput import CheckConstraintThroughput
from .check_constraint_throughput_ref import CheckConstraintThroughputRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintThroughputsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "checkConstraintThroughputs_RelStructure"

    check_constraint_throughput_ref: List[CheckConstraintThroughputRef] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintThroughputRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraint_throughput: List[CheckConstraintThroughput] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintThroughput",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
