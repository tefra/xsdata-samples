from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.add_hotel_pnr_element import AddHotelPnrElement
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.delete_hotel_pnr_element import DeleteHotelPnrElement
from travelport.models.update_hotel_pnr_element import UpdateHotelPnrElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingHotelPnrElementReq(BookingBaseReq):
    """
    Adds, Modifies hotel elements like Guarantee, BookingSource, etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_hotel_pnr_element: None | AddHotelPnrElement = field(
        default=None,
        metadata={
            "name": "AddHotelPnrElement",
            "type": "Element",
        }
    )
    update_hotel_pnr_element: None | UpdateHotelPnrElement = field(
        default=None,
        metadata={
            "name": "UpdateHotelPnrElement",
            "type": "Element",
        }
    )
    delete_hotel_pnr_element: None | DeleteHotelPnrElement = field(
        default=None,
        metadata={
            "name": "DeleteHotelPnrElement",
            "type": "Element",
        }
    )
