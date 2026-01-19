from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .controllable_element import ControllableElement
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "controllableElementsInFrame_RelStructure"

    controllable_element: Sequence[ControllableElement] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
