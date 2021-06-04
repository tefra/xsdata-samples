from dataclasses import dataclass, field
from typing import List
from netex.models.border_point import BorderPoint
from netex.models.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BorderPointsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "borderPointsInFrame_RelStructure"

    border_point: List[BorderPoint] = field(
        default_factory=list,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
