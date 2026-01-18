from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .fulfilment_method import FulfilmentMethod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FulfilmentMethodsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fulfilmentMethodsInFrame_RelStructure"

    fulfilment_method: Iterable[FulfilmentMethod] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
