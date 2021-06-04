from dataclasses import dataclass, field
from typing import List
from netex.models.customer_account import CustomerAccount
from netex.models.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customerAccountsInFrame_RelStructure"

    customer_account: List[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
