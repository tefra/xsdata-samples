from dataclasses import dataclass, field

from .customer_purchase_package_element_ref import (
    CustomerPurchasePackageElementRef,
)
from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackagePriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "CustomerPurchasePackagePrice_VersionedChildStructure"

    customer_purchase_package_ref_or_customer_purchase_package_element_ref: (
        CustomerPurchasePackageRef | CustomerPurchasePackageElementRef | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageElementRef",
                    "type": CustomerPurchasePackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
