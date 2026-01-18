from __future__ import annotations

from dataclasses import dataclass

from .fare_contract_security_listing_versioned_child_structure import (
    FareContractSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractSecurityListing(
    FareContractSecurityListingVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
