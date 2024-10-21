from collections.abc import Iterable
from dataclasses import dataclass, field

from .border_point import BorderPoint
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BorderPointsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "borderPointsInFrame_RelStructure"

    border_point: Iterable[BorderPoint] = field(
        default_factory=list,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
