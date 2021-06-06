from dataclasses import dataclass
from .customer_purchase_package_price_ref_structure import CustomerPurchasePackagePriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackagePriceRef(CustomerPurchasePackagePriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
