from dataclasses import dataclass, field
from typing import List
from .customer_purchase_package_element_access import (
    CustomerPurchasePackageElementAccess,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageElementAccessesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "customerPurchasePackageElementAccesses_RelStructure"

    customer_purchase_package_element_access: List[
        CustomerPurchasePackageElementAccess
    ] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElementAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
