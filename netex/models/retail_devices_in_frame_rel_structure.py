from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .retail_device import RetailDevice

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDevicesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "retailDevicesInFrame_RelStructure"

    retail_device: Iterable[RetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "RetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
