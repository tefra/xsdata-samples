from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_retrieve_document_req import AirRetrieveDocumentReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class AirRetrieveDocumentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | AirRetrieveDocumentPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        air_retrieve_document_req: None | AirRetrieveDocumentReq = field(
            default=None,
            metadata={
                "name": "AirRetrieveDocumentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/air_v52_0",
            },
        )
