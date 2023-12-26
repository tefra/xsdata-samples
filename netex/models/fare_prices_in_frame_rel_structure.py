from dataclasses import dataclass, field
from typing import List
from .cell_versioned_child_structure import PriceGroup
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePricesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "farePricesInFrame_RelStructure"

    price_group: List[PriceGroup] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
