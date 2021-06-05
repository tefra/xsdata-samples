from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.customer_account_security_listing import CustomerAccountSecurityListing
from netex.models.customer_security_listing import CustomerSecurityListing
from netex.models.fare_contract_security_listing import FareContractSecurityListing
from netex.models.retail_device_security_listing import RetailDeviceSecurityListing
from netex.models.security_listing_1 import SecurityListing1
from netex.models.security_listing_2 import SecurityListing2
from netex.models.travel_document_security_listing import TravelDocumentSecurityListing

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
            "min_occurs": 1,
        }
    )
    retail_device_security_listing: List[RetailDeviceSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_contract_security_listing: List[FareContractSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "FareContractSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_security_listing: List[CustomerSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "CustomerSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_account_security_listing: List[CustomerAccountSecurityListing] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountSecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    security_listing: List[SecurityListing1] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_security_listing: List[SecurityListing2] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListing_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
