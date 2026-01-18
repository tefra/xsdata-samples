from __future__ import annotations

from dataclasses import dataclass, field

from .fare_element_in_sequence_versioned_child_structure import (
    FareElementInSequenceVersionedChildStructure,
)
from .fare_structure_element_ref import FareStructureElementRef
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from .validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementInSequenceVersionedChildStructure(
    FareElementInSequenceVersionedChildStructure
):
    class Meta:
        name = "FareStructureElementInSequence_VersionedChildStructure"

    fare_structure_element_ref: None | FareStructureElementRef = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validable_element_ref: None | ValidableElementRef = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context: (
        None
        | GenericParameterAssignmentsRelStructure
        | GenericParameterAssignment
        | GenericParameterAssignmentInContext
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityParameterAssignments",
                    "type": GenericParameterAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
