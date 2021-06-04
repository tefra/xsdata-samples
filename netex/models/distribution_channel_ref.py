from dataclasses import dataclass
from netex.models.distribution_channel_ref_structure_element import DistributionChannelRefStructureElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionChannelRef(DistributionChannelRefStructureElement):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
