from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_purchase_parameter_assignment import (
    CustomerPurchaseParameterAssignment,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchaseParameterAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "customerPurchaseParameterAssignments_RelStructure"

    customer_purchase_parameter_assignment: Iterable[
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
