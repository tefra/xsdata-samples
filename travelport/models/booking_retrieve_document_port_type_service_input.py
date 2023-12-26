from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_retrieve_document_req import (
    BookingRetrieveDocumentReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class BookingRetrieveDocumentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    operation: None | BookingRetrieveDocumentPortTypeServiceInput.Operation = (
        field(
            default=None,
            metadata={
                "name": "Operation",
                "type": "Element",
            },
        )
    )
    body: None | BookingRetrieveDocumentPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Operation:
        booking_retrieve_document_req: None | BookingRetrieveDocumentReq = field(
            default=None,
            metadata={
                "name": "BookingRetrieveDocumentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            },
        )

    @dataclass
    class Body:
        booking_retrieve_document_req: None | BookingRetrieveDocumentReq = field(
            default=None,
            metadata={
                "name": "BookingRetrieveDocumentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            },
        )
