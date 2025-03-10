from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .activation_assignment import ActivationAssignment
from .activation_assignment_ref import ActivationAssignmentRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "activationAssignments_RelStructure"

    activation_assignment_ref_or_activation_assignment: Iterable[
        Union[ActivationAssignmentRef, ActivationAssignment]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ActivationAssignmentRef",
                    "type": ActivationAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationAssignment",
                    "type": ActivationAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
