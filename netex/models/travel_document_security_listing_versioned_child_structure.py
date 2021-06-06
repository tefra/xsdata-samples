from dataclasses import dataclass, field
from typing import Optional
from .security_listing_versioned_child_structure import SecurityListingVersionedChildStructure
from .travel_document_ref import TravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelDocumentSecurityListingVersionedChildStructure(SecurityListingVersionedChildStructure):
    class Meta:
        name = "TravelDocumentSecurityListing_VersionedChildStructure"

    travel_document_ref: Optional[TravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
