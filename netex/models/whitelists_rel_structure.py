from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .whitelist import Whitelist
from .whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WhitelistsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "whitelists_RelStructure"

    whitelist_ref: List[WhitelistRef] = field(
        default_factory=list,
        metadata={
            "name": "WhitelistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    whitelist: List[Whitelist] = field(
        default_factory=list,
        metadata={
            "name": "Whitelist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )