from __future__ import annotations

from dataclasses import dataclass

from .customer_purchase_package_price_versioned_child_structure import (
    CustomerPurchasePackagePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagePrice(
    CustomerPurchasePackagePriceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
