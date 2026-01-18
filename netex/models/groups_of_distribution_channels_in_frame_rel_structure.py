from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .group_of_distribution_channels import GroupOfDistributionChannels

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfDistributionChannelsInFrameRelStructure(
    FrameContainmentStructure
):
    class Meta:
        name = "groupsOfDistributionChannelsInFrame_RelStructure"

    group_of_distribution_channels: Iterable[GroupOfDistributionChannels] = (
        field(
            default_factory=list,
            metadata={
                "name": "GroupOfDistributionChannels",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
