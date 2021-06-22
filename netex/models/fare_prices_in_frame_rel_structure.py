from dataclasses import dataclass, field
from typing import List
from .cell_versioned_child_structure import PriceGroup1
from .frame_containment_structure import FrameContainmentStructure
from .price_group_2 import PriceGroup2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePricesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "farePricesInFrame_RelStructure"

    price_group_or_price_group: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PriceGroup",
                    "type": PriceGroup1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceGroup_",
                    "type": PriceGroup2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
