from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_traveler_req import BookingTravelerReq
from travelport.models.session_context import SessionContext

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass
class BookingTravelerPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: None | BookingTravelerPortTypeServiceInput.Header = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        },
    )
    body: None | BookingTravelerPortTypeServiceInput.Body = field(
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
        booking_traveler_req: None | BookingTravelerReq = field(
            default=None,
            metadata={
                "name": "BookingTravelerReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            },
        )
