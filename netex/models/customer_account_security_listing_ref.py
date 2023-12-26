from dataclasses import dataclass
from .customer_account_security_listing_ref_structure import (
    CustomerAccountSecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerAccountSecurityListingRef(
    CustomerAccountSecurityListingRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
