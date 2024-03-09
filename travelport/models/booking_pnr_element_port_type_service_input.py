from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_pnr_element_req import BookingPnrElementReq
from travelport.models.session_context import SessionContext

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class BookingPnrElementPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | BookingPnrElementPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | BookingPnrElementPortTypeServiceInput.Body = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Header:
        session_context: None | SessionContext = field(
            default=None,
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            },
        )

    @dataclass
    class Body:
        booking_pnr_element_req: None | BookingPnrElementReq = field(
            default=None,
            metadata={
                "name": "BookingPnrElementReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            },
        )
