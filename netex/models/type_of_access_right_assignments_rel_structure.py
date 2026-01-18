from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_access_right_assignment import TypeOfAccessRightAssignment
from .type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfAccessRightAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "TypeOfAccessRightAssignments_RelStructure"

    type_of_access_right_assignment_ref_or_type_of_access_right_assignment: Iterable[
        TypeOfAccessRightAssignmentRef | TypeOfAccessRightAssignment
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfAccessRightAssignmentRef",
                    "type": TypeOfAccessRightAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignment",
                    "type": TypeOfAccessRightAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
