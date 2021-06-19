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

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WhitelistRef",
                    "type": WhitelistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlacklistRef",
                    "type": BlacklistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SecurityListRef",
                    "type": SecurityListRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SecurityList",
                    "type": SecurityList,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
