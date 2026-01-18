from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .sections_in_sequence_rel_structure import FareSection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareSectionsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareSectionsInFrame_RelStructure"

    fare_section: Iterable[FareSection] = field(
        default_factory=list,
        metadata={
            "name": "FareSection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
