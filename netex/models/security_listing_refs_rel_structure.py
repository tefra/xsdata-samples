from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .customer_account_security_listing_ref import (
    CustomerAccountSecurityListingRef,
)
from .customer_security_listing_ref import CustomerSecurityListingRef
from .fare_contract_security_listing_ref import FareContractSecurityListingRef
from .medium_access_device_security_listing_ref import (
    MediumAccessDeviceSecurityListingRef,
)
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .retail_device_security_listing_ref import RetailDeviceSecurityListingRef
from .travel_document_security_listing_ref import (
    TravelDocumentSecurityListingRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "SecurityListingRefs_RelStructure"

    security_listing_ref: Iterable[
        TravelDocumentSecurityListingRef
        | MediumAccessDeviceSecurityListingRef
        | RetailDeviceSecurityListingRef
        | CustomerAccountSecurityListingRef
        | FareContractSecurityListingRef
        | CustomerSecurityListingRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TravelDocumentSecurityListingRef",
                    "type": TravelDocumentSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MediumAccessDeviceSecurityListingRef",
                    "type": MediumAccessDeviceSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDeviceSecurityListingRef",
                    "type": RetailDeviceSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountSecurityListingRef",
                    "type": CustomerAccountSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractSecurityListingRef",
                    "type": FareContractSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerSecurityListingRef",
                    "type": CustomerSecurityListingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
