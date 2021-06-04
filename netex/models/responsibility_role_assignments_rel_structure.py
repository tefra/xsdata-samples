from dataclasses import dataclass, field
from typing import List
from netex.models.responsibility_role_assignment import ResponsibilityRoleAssignment
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilityRoleAssignmentsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "responsibilityRoleAssignments_RelStructure"

    responsibility_role_assignment: List[ResponsibilityRoleAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ResponsibilityRoleAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
