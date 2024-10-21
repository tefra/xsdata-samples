from collections.abc import Iterable
from dataclasses import dataclass, field

from .customer_account import CustomerAccount
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customerAccountsInFrame_RelStructure"

    customer_account: Iterable[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
