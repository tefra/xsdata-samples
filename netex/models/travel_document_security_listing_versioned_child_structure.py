from dataclasses import dataclass, field
from typing import Optional, Union

from .security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)
from .service_access_code_ref import ServiceAccessCodeRef
from .travel_document_ref import TravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelDocumentSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    class Meta:
        name = "TravelDocumentSecurityListing_VersionedChildStructure"

    travel_document_ref: ServiceAccessCodeRef | TravelDocumentRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceAccessCodeRef",
                    "type": ServiceAccessCodeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocumentRef",
                    "type": TravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
