from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .customer_purchase_package import CustomerPurchasePackage
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchasePackagesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customerPurchasePackagesInFrame_RelStructure"

    customer_purchase_package: Sequence[CustomerPurchasePackage] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
