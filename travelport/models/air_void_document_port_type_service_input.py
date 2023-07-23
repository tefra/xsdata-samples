from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_void_document_req import AirVoidDocumentReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirVoidDocumentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirVoidDocumentPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        air_void_document_req: None | AirVoidDocumentReq = field(
            default=None,
            metadata={
                "name": "AirVoidDocumentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            }
        )
