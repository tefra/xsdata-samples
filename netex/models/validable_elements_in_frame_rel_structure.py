from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .validable_element import ValidableElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElementsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "validableElementsInFrame_RelStructure"

    validable_element: Iterable[ValidableElement] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
