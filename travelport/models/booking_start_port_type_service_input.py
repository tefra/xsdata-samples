from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.booking_start_req import BookingStartReq

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class BookingStartPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: None | BookingStartPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        booking_start_req: None | BookingStartReq = field(
            default=None,
            metadata={
                "name": "BookingStartReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            },
        )
