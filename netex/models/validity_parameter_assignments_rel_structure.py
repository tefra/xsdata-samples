from dataclasses import dataclass, field
from typing import List, Union
from .access_right_parameter_assignment import AccessRightParameterAssignment
from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_purchase_parameter_assignment import CustomerPurchaseParameterAssignment
from .generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from .specific_parameter_assignment_version_structure import SpecificParameterAssignment
from .validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityParameterAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "validityParameterAssignments_RelStructure"

    choice: List[Union[CustomerPurchaseParameterAssignment, SpecificParameterAssignment, GenericParameterAssignmentInContext, GenericParameterAssignment, ValidityParameterAssignment, AccessRightParameterAssignment]] = field(
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
                    "type": AccessRightParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
