from collections.abc import Iterable
from dataclasses import dataclass, field

from .check_constraint_throughput import CheckConstraintThroughput
from .check_constraint_throughput_ref import CheckConstraintThroughputRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintThroughputsRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "checkConstraintThroughputs_RelStructure"

    check_constraint_throughput_ref_or_check_constraint_throughput: Iterable[
        CheckConstraintThroughputRef | CheckConstraintThroughput
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CheckConstraintThroughputRef",
                    "type": CheckConstraintThroughputRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintThroughput",
                    "type": CheckConstraintThroughput,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
