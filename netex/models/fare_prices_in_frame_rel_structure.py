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

    price_group: List[PriceGroup1] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_price_group: List[PriceGroup2] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
