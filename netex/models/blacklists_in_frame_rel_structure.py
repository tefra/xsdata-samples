from dataclasses import dataclass, field
from typing import List
from .blacklist import Blacklist
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlacklistsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "blacklistsInFrame_RelStructure"

    blacklist: List[Blacklist] = field(
        default_factory=list,
        metadata={
            "name": "Blacklist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
