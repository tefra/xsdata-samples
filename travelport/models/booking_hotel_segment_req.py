from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.add_hotel_segment import AddHotelSegment
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.delete_hotel_segment import DeleteHotelSegment

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingHotelSegmentReq(BookingBaseReq):
    """
    Used for Hotel Segment Sell and modification.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_hotel_segment: None | AddHotelSegment = field(
        default=None,
        metadata={
            "name": "AddHotelSegment",
            "type": "Element",
        }
    )
    delete_hotel_segment: None | DeleteHotelSegment = field(
        default=None,
        metadata={
            "name": "DeleteHotelSegment",
            "type": "Element",
        }
    )
