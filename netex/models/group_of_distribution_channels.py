from dataclasses import dataclass
from netex.models.group_of_distribution_channels_version_structure import GroupOfDistributionChannelsVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfDistributionChannels(GroupOfDistributionChannelsVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
