from dataclasses import dataclass, field
from typing import List
from .fare_contract_security_listing_ref import FareContractSecurityListingRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractSecurityListingRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "FareContractSecurityListingRefs_RelStructure"

    fare_contract_security_listing_ref: List[
        FareContractSecurityListingRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "FareContractSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
