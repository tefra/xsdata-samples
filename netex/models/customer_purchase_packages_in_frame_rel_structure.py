from dataclasses import dataclass, field
from typing import List
from netex.models.customer_purchase_package import CustomerPurchasePackage
from netex.models.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerPurchasePackagesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customerPurchasePackagesInFrame_RelStructure"

    customer_purchase_package: List[CustomerPurchasePackage] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
