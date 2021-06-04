from dataclasses import dataclass, field
from typing import List
from netex.models.distribution_channel_ref import DistributionChannelRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionChannelRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "distributionChannelRefs_RelStructure"

    distribution_channel_ref: List[DistributionChannelRef] = field(
        default_factory=list,
        metadata={
            "name": "DistributionChannelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
