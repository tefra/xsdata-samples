from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .frame_containment_structure import FrameContainmentStructure
from .service_access_code import ServiceAccessCode
from .service_access_code_ref import ServiceAccessCodeRef
from .travel_document import TravelDocument
from .travel_document_ref import TravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelDocumentsRelStructure(FrameContainmentStructure):
    class Meta:
        name = "travelDocuments_RelStructure"

    choice: Iterable[
        ServiceAccessCodeRef | TravelDocumentRef | TravelDocument | ServiceAccessCode
    ] = field(
        default_factory=list,
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
                {
                    "name": "TravelDocument",
                    "type": TravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessCode",
                    "type": ServiceAccessCode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
