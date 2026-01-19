from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .border_point import BorderPoint
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "borderPointsInFrame_RelStructure"

    border_point: Sequence[BorderPoint] = field(
        default_factory=list,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
