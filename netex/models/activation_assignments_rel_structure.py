from dataclasses import dataclass, field
from typing import List
from netex.models.activation_assignment import ActivationAssignment
from netex.models.activation_assignment_ref import ActivationAssignmentRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "activationAssignments_RelStructure"

    activation_assignment_ref: List[ActivationAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "ActivationAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_assignment: List[ActivationAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ActivationAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
