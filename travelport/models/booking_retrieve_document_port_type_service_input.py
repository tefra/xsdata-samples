from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_retrieve_document_req import (
    BookingRetrieveDocumentReq,
)

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class BookingRetrieveDocumentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    operation: BookingRetrieveDocumentPortTypeServiceInput.Operation = field(
        metadata={
            "name": "Operation",
            "type": "Element",
        }
    )
    body: BookingRetrieveDocumentPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Operation:
        booking_retrieve_document_req: BookingRetrieveDocumentReq = field(
            metadata={
                "name": "BookingRetrieveDocumentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            }
        )

    @dataclass(kw_only=True)
    class Body:
        booking_retrieve_document_req: BookingRetrieveDocumentReq = field(
            metadata={
                "name": "BookingRetrieveDocumentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            }
        )
