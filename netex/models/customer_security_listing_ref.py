from dataclasses import dataclass
from .customer_security_listing_ref_structure import CustomerSecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerSecurityListingRef(CustomerSecurityListingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
