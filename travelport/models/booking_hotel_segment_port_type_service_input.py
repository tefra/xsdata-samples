from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.booking_hotel_segment_req import BookingHotelSegmentReq
from travelport.models.session_context import SessionContext

__NAMESPACE__ = "http://www.travelport.com/service/air_v52_0"


@dataclass(kw_only=True)
class BookingHotelSegmentPortTypeServiceInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: BookingHotelSegmentPortTypeServiceInput.Header = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    body: BookingHotelSegmentPortTypeServiceInput.Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Header:
        session_context: SessionContext = field(
            metadata={
                "name": "SessionContext",
                "type": "Element",
                "namespace": "http://www.travelport.com/soa/common/security/SessionContext_v1",
            }
        )

    @dataclass(kw_only=True)
    class Body:
        booking_hotel_segment_req: BookingHotelSegmentReq = field(
            metadata={
                "name": "BookingHotelSegmentReq",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedBooking_v52_0",
            }
        )
