from dataclasses import dataclass
from .all_distribution_channels_ref_structure_element import (
    AllDistributionChannelsRefStructureElement,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllDistributionChannelsRef(AllDistributionChannelsRefStructureElement):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
