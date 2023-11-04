from dataclasses import dataclass, field
from typing import List, Union
from .blacklist_ref import BlacklistRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecurityListsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "securityLists_RelStructure"

    whitelist_ref_or_blacklist_ref: List[Union[WhitelistRef, BlacklistRef]] = field(
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
            ),
        }
    )
