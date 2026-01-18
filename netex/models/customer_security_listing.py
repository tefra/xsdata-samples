from __future__ import annotations

from dataclasses import dataclass

from .customer_security_listing_versioned_child_structure import (
    CustomerSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerSecurityListing(CustomerSecurityListingVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
