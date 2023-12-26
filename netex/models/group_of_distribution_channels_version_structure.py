from dataclasses import dataclass, field
from typing import Optional
from .distribution_channel_refs_rel_structure import (
    DistributionChannelRefsRelStructure,
)
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfDistributionChannelsVersionStructure(
    GroupOfEntitiesVersionStructure
):
    class Meta:
        name = "GroupOfDistributionChannels_VersionStructure"

    members: Optional[DistributionChannelRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
