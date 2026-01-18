from __future__ import annotations

from dataclasses import dataclass

from .distribution_channel_version_structure import (
    DistributionChannelVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionChannel(DistributionChannelVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
