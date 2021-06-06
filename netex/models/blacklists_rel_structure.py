from dataclasses import dataclass, field
from typing import List
from .blacklist import Blacklist
from .blacklist_ref import BlacklistRef
from .containment_aggregation_structure import ContainmentAggregationStructure

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
