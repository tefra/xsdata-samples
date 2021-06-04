from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.customer_purchase_package_element import CustomerPurchasePackageElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageElementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "customerPurchasePackageElements_RelStructure"

    customer_purchase_package_element: List[CustomerPurchasePackageElement] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
