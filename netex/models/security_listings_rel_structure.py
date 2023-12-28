from dataclasses import dataclass, field
from typing import List, Union
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

    security_listing: List[
        Union[
            TravelDocumentSecurityListing,
            RetailDeviceSecurityListing,
            FareContractSecurityListing,
            CustomerSecurityListing,
            CustomerAccountSecurityListing,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TravelDocumentSecurityListing",
                    "type": TravelDocumentSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDeviceSecurityListing",
                    "type": RetailDeviceSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractSecurityListing",
                    "type": FareContractSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerSecurityListing",
                    "type": CustomerSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountSecurityListing",
                    "type": CustomerAccountSecurityListing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
