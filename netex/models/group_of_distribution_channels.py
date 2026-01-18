from __future__ import annotations

from dataclasses import dataclass

from .group_of_distribution_channels_version_structure import (
    GroupOfDistributionChannelsVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfDistributionChannels(GroupOfDistributionChannelsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
