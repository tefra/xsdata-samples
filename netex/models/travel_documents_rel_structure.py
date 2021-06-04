from dataclasses import dataclass, field
from typing import List
from netex.models.frame_containment_structure import FrameContainmentStructure
from netex.models.travel_document import TravelDocument
from netex.models.travel_document_ref import TravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelDocumentsRelStructure(FrameContainmentStructure):
    class Meta:
        name = "travelDocuments_RelStructure"

    travel_document_ref: List[TravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
