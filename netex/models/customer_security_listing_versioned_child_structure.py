from dataclasses import dataclass, field
from typing import Optional
from netex.models.customer_ref import CustomerRef
from netex.models.security_listing_versioned_child_structure import SecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerSecurityListingVersionedChildStructure(SecurityListingVersionedChildStructure):
    class Meta:
        name = "CustomerSecurityListing_VersionedChildStructure"

    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
