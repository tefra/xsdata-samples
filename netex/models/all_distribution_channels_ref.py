from __future__ import annotations

from dataclasses import dataclass

from .all_distribution_channels_ref_structure_element import (
    AllDistributionChannelsRefStructureElement,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllDistributionChannelsRef(AllDistributionChannelsRefStructureElement):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
