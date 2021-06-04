from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.display_assignment import DisplayAssignment
from netex.models.display_assignment_ref import DisplayAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DisplayAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "displayAssignments_RelStructure"

    display_assignment_ref: List[DisplayAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "DisplayAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    display_assignment: List[DisplayAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DisplayAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
