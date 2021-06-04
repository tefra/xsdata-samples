from dataclasses import dataclass, field
from typing import List
from netex.models.blacklist import Blacklist
from netex.models.blacklist_ref import BlacklistRef
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlacklistsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "blacklists_RelStructure"

    blacklist_ref: List[BlacklistRef] = field(
        default_factory=list,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    blacklist: List[Blacklist] = field(
        default_factory=list,
        metadata={
            "name": "Blacklist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
