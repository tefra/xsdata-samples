from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .individual_traveller import IndividualTraveller

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class IndividualTravellersInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "individualTravellersInFrame_RelStructure"

    individual_traveller: Iterable[IndividualTraveller] = field(
        default_factory=list,
        metadata={
            "name": "IndividualTraveller",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
