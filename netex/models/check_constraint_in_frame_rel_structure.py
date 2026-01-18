from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .check_constraint import CheckConstraint
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CheckConstraintInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "checkConstraintInFrame_RelStructure"

    check_constraint: Iterable[CheckConstraint] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
