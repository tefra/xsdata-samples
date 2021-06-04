from dataclasses import dataclass, field
from typing import Optional
from netex.models.customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from netex.models.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.models.fare_price_versioned_child_structure import FarePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackagePriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "CustomerPurchasePackagePrice_VersionedChildStructure"

    customer_purchase_package_ref: Optional[CustomerPurchasePackageRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_element_ref: Optional[CustomerPurchasePackageElementRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
