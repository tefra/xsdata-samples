from __future__ import annotations

from dataclasses import dataclass

from .customer_purchase_parameter_assignment_version_structure import (
    CustomerPurchaseParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchaseParameterAssignment(
    CustomerPurchaseParameterAssignmentVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
