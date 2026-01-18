from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .fare_zone import FareZone
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareZonesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareZonesInFrame_RelStructure"

    fare_zone: Iterable[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
