from dataclasses import dataclass, field
from typing import List
from netex.models.frame_containment_structure import FrameContainmentStructure
from netex.models.sales_transaction import SalesTransaction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesTransactionsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "salesTransactionsInFrame_RelStructure"

    sales_transaction: List[SalesTransaction] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransaction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
