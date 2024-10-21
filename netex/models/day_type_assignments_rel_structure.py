from collections.abc import Iterable
from dataclasses import dataclass, field

from .day_type_assignment import DayTypeAssignment
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DayTypeAssignmentsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "dayTypeAssignments_RelStructure"

    day_type_assignment: Iterable[DayTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
