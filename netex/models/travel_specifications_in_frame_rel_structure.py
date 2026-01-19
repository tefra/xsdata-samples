from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .travel_specification_1 import TravelSpecification1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecificationsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "travelSpecificationsInFrame_RelStructure"

    travel_specification: Sequence[TravelSpecification1] = field(
        default_factory=list,
        metadata={
            "name": "TravelSpecification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
