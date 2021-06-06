from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .travel_document_security_listing_ref import TravelDocumentSecurityListingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelDocumentSecurityListingRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "TravelDocumentSecurityListingRefs_RelStructure"

    travel_document_security_listing_ref: List[TravelDocumentSecurityListingRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentSecurityListingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
