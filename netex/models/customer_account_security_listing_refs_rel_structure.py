from dataclasses import dataclass, field
from typing import List
from .customer_account_security_listing_ref import CustomerAccountSecurityListingRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "customerAccountSecurityListingRefs_RelStructure"

    customer_account_security_listing_ref: List[CustomerAccountSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
