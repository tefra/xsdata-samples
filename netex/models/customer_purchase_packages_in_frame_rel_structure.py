from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .customer_purchase_package import CustomerPurchasePackage
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackagesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customerPurchasePackagesInFrame_RelStructure"

    customer_purchase_package: Iterable[CustomerPurchasePackage] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
