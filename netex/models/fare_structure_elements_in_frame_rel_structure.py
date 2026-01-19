from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .fare_structure_element import FareStructureElement
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareStructureElementsInFrame_RelStructure"

    fare_structure_element: Sequence[FareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
