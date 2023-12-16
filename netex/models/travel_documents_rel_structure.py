from dataclasses import dataclass, field
from typing import List, Union
from .frame_containment_structure import FrameContainmentStructure
from .travel_document import TravelDocument
from .travel_document_ref import TravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelDocumentsRelStructure(FrameContainmentStructure):
    class Meta:
        name = "travelDocuments_RelStructure"

    travel_document_ref_or_travel_document: List[Union[TravelDocumentRef, TravelDocument]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TravelDocumentRef",
                    "type": TravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelDocument",
                    "type": TravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
