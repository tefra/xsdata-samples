from dataclasses import dataclass
from .travel_document_security_listing_versioned_child_structure import (
    TravelDocumentSecurityListingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelDocumentSecurityListing(
    TravelDocumentSecurityListingVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
