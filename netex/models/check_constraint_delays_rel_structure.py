from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .check_constraint_delay import CheckConstraintDelay
from .check_constraint_delay_ref import CheckConstraintDelayRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CheckConstraintDelaysRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "checkConstraintDelays_RelStructure"

    check_constraint_delay_ref_or_check_constraint_delay: Iterable[
        CheckConstraintDelayRef | CheckConstraintDelay
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CheckConstraintDelayRef",
                    "type": CheckConstraintDelayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintDelay",
                    "type": CheckConstraintDelay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
