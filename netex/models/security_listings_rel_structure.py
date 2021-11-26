from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .customer_account_security_listing import CustomerAccountSecurityListing
from .customer_security_listing import CustomerSecurityListing
from .fare_contract_security_listing import FareContractSecurityListing
from .retail_device_security_listing import RetailDeviceSecurityListing
from .travel_document_security_listing import TravelDocumentSecurityListing

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecurityListingsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "securityListings_RelStructure"

    travel_document_security_listing: List[TravelDocumentSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_device_security_listing: List[RetailDeviceSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_contract_security_listing: List[FareContractSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "FareContractSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_security_listing: List[CustomerSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "CustomerSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_account_security_listing: List[CustomerAccountSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
