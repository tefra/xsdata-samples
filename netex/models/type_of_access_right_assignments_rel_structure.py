from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.type_of_access_right_assignment import TypeOfAccessRightAssignment
from netex.models.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfAccessRightAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "TypeOfAccessRightAssignments_RelStructure"

    type_of_access_right_assignment_ref: List[TypeOfAccessRightAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_access_right_assignment: List[TypeOfAccessRightAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfAccessRightAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
