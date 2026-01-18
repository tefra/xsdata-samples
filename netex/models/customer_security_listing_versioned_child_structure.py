from dataclasses import dataclass, field

from .customer_ref import CustomerRef
from .security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    class Meta:
        name = "CustomerSecurityListing_VersionedChildStructure"

    customer_ref: CustomerRef | None = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
