from dataclasses import dataclass, field
from typing import List, Union

from .access_right_parameter_assignment_1 import (
    AccessRightParameterAssignment1,
)
from .customer_purchase_parameter_assignment import (
    CustomerPurchaseParameterAssignment,
)
from .frame_containment_structure import FrameContainmentStructure
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from .specific_parameter_assignments_rel_structure import (
    SpecificParameterAssignment,
)
from .validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightParameterAssignmentsInFrameRelStructure(
    FrameContainmentStructure
):
    class Meta:
        name = "accessRightParameterAssignmentsInFrame_RelStructure"

    access_right_parameter_assignment: List[
        Union[
            CustomerPurchaseParameterAssignment,
            SpecificParameterAssignment,
            GenericParameterAssignmentInContext,
            GenericParameterAssignment,
            ValidityParameterAssignment,
            AccessRightParameterAssignment1,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchaseParameterAssignment",
                    "type": CustomerPurchaseParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecificParameterAssignment",
                    "type": SpecificParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityParameterAssignment",
                    "type": ValidityParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightParameterAssignment",
                    "type": AccessRightParameterAssignment1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
