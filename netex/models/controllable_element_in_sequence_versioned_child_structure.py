from dataclasses import dataclass, field
from typing import Optional

from .access_right_parameter_assignments_rel_structure import (
    AccessRightParameterAssignmentsRelStructure,
)
from .controllable_element_ref import ControllableElementRef
from .fare_element_in_sequence_versioned_child_structure import (
    FareElementInSequenceVersionedChildStructure,
)
from .fare_structure_element_ref import FareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementInSequenceVersionedChildStructure(
    FareElementInSequenceVersionedChildStructure
):
    class Meta:
        name = "ControllableElementInSequence_VersionedChildStructure"

    controllable_element_ref: Optional[ControllableElementRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_right_parameter_assignments: Optional[
        AccessRightParameterAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "accessRightParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
