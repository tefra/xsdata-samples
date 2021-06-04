from dataclasses import dataclass, field
from typing import List
from netex.models.blacklist_ref import BlacklistRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.security_list_ref import SecurityListRef
from netex.models.whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecuritylistRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "securitylistRefs_RelStructure"

    whitelist_ref: List[WhitelistRef] = field(
        default_factory=list,
        metadata={
            "name": "WhitelistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    blacklist_ref: List[BlacklistRef] = field(
        default_factory=list,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    security_list_ref: List[SecurityListRef] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
