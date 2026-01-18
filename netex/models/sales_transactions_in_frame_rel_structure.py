from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .sales_transaction import SalesTransaction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesTransactionsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "salesTransactionsInFrame_RelStructure"

    sales_transaction: Iterable[SalesTransaction] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransaction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
