from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .rounding_step import RoundingStep
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundingStepsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "roundingSteps_RelStructure"

    rounding_step: Iterable[RoundingStep] = field(
        default_factory=list,
        metadata={
            "name": "RoundingStep",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
