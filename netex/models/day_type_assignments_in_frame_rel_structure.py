from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .day_type_assignment import DayTypeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DayTypeAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dayTypeAssignmentsInFrame_RelStructure"

    day_type_assignment: Iterable[DayTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
