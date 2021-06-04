from dataclasses import dataclass, field
from typing import List
from netex.models.blacklist_ref import BlacklistRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BlacklistRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "blacklistRefs_RelStructure"

    blacklist_ref: List[BlacklistRef] = field(
        default_factory=list,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
