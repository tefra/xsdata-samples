from dataclasses import dataclass
from .travel_document_security_listing_ref_structure import (
    TravelDocumentSecurityListingRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelDocumentSecurityListingRef(
    TravelDocumentSecurityListingRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
