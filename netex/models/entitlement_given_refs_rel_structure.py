from dataclasses import dataclass, field
from typing import List
from .entitlement_given_ref import EntitlementGivenRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementGivenRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "entitlementGivenRefs_RelStructure"

    entitlement_given_ref: List[EntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
