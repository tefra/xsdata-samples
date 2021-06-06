from dataclasses import dataclass, field
from typing import Optional
from .customer_account_ref import CustomerAccountRef
from .security_listing_versioned_child_structure import SecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountSecurityListingVersionedChildStructure(SecurityListingVersionedChildStructure):
    class Meta:
        name = "CustomerAccountSecurityListing_VersionedChildStructure"

    customer_account_ref: Optional[CustomerAccountRef] = field(
        default=None,
        metadata={
            "name": "CustomerAccountRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
