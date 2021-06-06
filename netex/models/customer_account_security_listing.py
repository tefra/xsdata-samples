from dataclasses import dataclass
from .customer_account_security_listing_versioned_child_structure import CustomerAccountSecurityListingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountSecurityListing(CustomerAccountSecurityListingVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
