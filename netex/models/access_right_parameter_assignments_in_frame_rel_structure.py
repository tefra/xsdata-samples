from dataclasses import dataclass, field
from typing import List
from .access_right_parameter_assignment_1 import AccessRightParameterAssignment1
from .access_right_parameter_assignment_2 import AccessRightParameterAssignment2
from .customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from .frame_containment_structure import FrameContainmentStructure
from .generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from .specific_parameter_assignment_version_structure import SpecificParameterAssignment
from .validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightParameterAssignmentsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "accessRightParameterAssignmentsInFrame_RelStructure"

    customer_purchase_parameter_assignment: List[CustomerPurchaseParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchaseParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    specific_parameter_assignment: List[SpecificParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment_in_context: List[GenericParameterAssignmentInContext] = field(
        default_factory=list,
        metadata={
            "name": "GenericParameterAssignmentInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment: List[GenericParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "GenericParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignment: List[ValidityParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ValidityParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_right_parameter_assignment: List[AccessRightParameterAssignment1] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_access_right_parameter_assignment: List[AccessRightParameterAssignment2] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightParameterAssignment_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
