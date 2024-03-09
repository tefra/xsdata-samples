from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_purchase_parameter_assignment import (
    CustomerPurchaseParameterAssignment,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchaseParameterAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "customerPurchaseParameterAssignments_RelStructure"

    customer_purchase_parameter_assignment: List[
        CustomerPurchaseParameterAssignment
    ] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchaseParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
