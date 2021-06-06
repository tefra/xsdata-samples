from dataclasses import dataclass, field
from typing import Optional
from .fare_contract_ref import FareContractRef
from .security_listing_versioned_child_structure import SecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractSecurityListingVersionedChildStructure(SecurityListingVersionedChildStructure):
    class Meta:
        name = "FareContractSecurityListing_VersionedChildStructure"

    fare_contract_ref: Optional[FareContractRef] = field(
        default=None,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
