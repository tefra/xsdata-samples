from dataclasses import dataclass, field
from typing import List
from .frame_containment_structure import FrameContainmentStructure
from .whitelist import Whitelist

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WhitelistsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "whitelistsInFrame_RelStructure"

    whitelist: List[Whitelist] = field(
        default_factory=list,
        metadata={
            "name": "Whitelist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
