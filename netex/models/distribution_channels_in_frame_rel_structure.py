from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .distribution_channel import DistributionChannel
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionChannelsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "distributionChannelsInFrame_RelStructure"

    distribution_channel: Iterable[DistributionChannel] = field(
        default_factory=list,
        metadata={
            "name": "DistributionChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
