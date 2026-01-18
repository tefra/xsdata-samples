from __future__ import annotations

from dataclasses import dataclass, field

from .customer_account_ref import CustomerAccountRef
from .security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    class Meta:
        name = "CustomerAccountSecurityListing_VersionedChildStructure"

    customer_account_ref: None | CustomerAccountRef = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
