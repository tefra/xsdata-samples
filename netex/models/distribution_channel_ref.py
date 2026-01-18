from __future__ import annotations

from dataclasses import dataclass

from .distribution_channel_ref_structure_element import (
    DistributionChannelRefStructureElement,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionChannelRef(DistributionChannelRefStructureElement):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
