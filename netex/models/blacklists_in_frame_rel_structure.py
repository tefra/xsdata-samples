from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .blacklist import Blacklist
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlacklistsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "blacklistsInFrame_RelStructure"

    blacklist: Sequence[Blacklist] = field(
        default_factory=list,
        metadata={
            "name": "Blacklist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
