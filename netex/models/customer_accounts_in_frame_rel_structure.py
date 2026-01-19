from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .customer_account import CustomerAccount
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "customerAccountsInFrame_RelStructure"

    customer_account: Sequence[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
