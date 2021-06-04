from dataclasses import dataclass
from netex.models.group_of_distribution_channels_ref_structure import GroupOfDistributionChannelsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfDistributionChannelsRef(GroupOfDistributionChannelsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
