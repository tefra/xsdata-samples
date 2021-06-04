from dataclasses import dataclass
from netex.models.fare_contract_security_listing_ref_structure import FareContractSecurityListingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractSecurityListingRef(FareContractSecurityListingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
