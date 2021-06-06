from dataclasses import dataclass, field
from typing import List
from .blacklist_ref import BlacklistRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .security_list import SecurityList
from .security_list_ref import SecurityListRef
from .whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecurityListsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "securityLists_RelStructure"

    whitelist_ref: List[WhitelistRef] = field(
        default_factory=list,
        metadata={
            "name": "WhitelistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    blacklist_ref: List[BlacklistRef] = field(
        default_factory=list,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    security_list_ref: List[SecurityListRef] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    security_list: List[SecurityList] = field(
        default_factory=list,
        metadata={
            "name": "SecurityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
