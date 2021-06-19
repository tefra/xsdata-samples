from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .display_assignment import DisplayAssignment
from .display_assignment_ref import DisplayAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DisplayAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "displayAssignments_RelStructure"

    display_assignment_ref_or_display_assignment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DisplayAssignmentRef",
                    "type": DisplayAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DisplayAssignment",
                    "type": DisplayAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
