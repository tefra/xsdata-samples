from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .type_of_travel_document import TypeOfTravelDocument

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfTravelDocumentInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "typesOfTravelDocumentInFrame_RelStructure"

    type_of_travel_document: Iterable[TypeOfTravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
