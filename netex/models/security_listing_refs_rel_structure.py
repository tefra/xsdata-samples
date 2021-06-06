from dataclasses import dataclass, field
from typing import List
from .customer_account_security_listing_ref import CustomerAccountSecurityListingRef
from .customer_security_listing_ref import CustomerSecurityListingRef
from .fare_contract_security_listing_ref import FareContractSecurityListingRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .retail_device_security_listing_ref import RetailDeviceSecurityListingRef
from .security_listing_ref import SecurityListingRef
from .travel_document_security_listing_ref import TravelDocumentSecurityListingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "SecurityListingRefs_RelStructure"

    travel_document_security_listing_ref: List[TravelDocumentSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    retail_device_security_listing_ref: List[RetailDeviceSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailDeviceSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_account_security_listing_ref: List[CustomerAccountSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccountSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_contract_security_listing_ref: List[FareContractSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    customer_security_listing_ref: List[CustomerSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    security_listing_ref: List[SecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "SecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
