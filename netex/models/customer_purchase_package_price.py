from dataclasses import dataclass
from .customer_purchase_package_price_versioned_child_structure import CustomerPurchasePackagePriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackagePrice(CustomerPurchasePackagePriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
