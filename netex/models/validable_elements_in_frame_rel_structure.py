from dataclasses import dataclass, field
from typing import List
from netex.models.frame_containment_structure import FrameContainmentStructure
from netex.models.validable_element import ValidableElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidableElementsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "validableElementsInFrame_RelStructure"

    validable_element: List[ValidableElement] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
