from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .fare_structure_element import FareStructureElement
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareStructureElementsInFrame_RelStructure"

    fare_structure_element: Iterable[FareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
