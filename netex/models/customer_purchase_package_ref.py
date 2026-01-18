from __future__ import annotations

from dataclasses import dataclass

from .customer_purchase_package_ref_structure import (
    CustomerPurchasePackageRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackageRef(CustomerPurchasePackageRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
