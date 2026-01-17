from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.add_air_pnr_element import AddAirPnrElement
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.delete_air_pnr_element import DeleteAirPnrElement
from travelport.models.update_air_pnr_element import UpdateAirPnrElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingAirPnrElementReq(BookingBaseReq):
    """
    Adds, Modifies air elements like Stored fare FOP, Credit Card Auth,
    Ticketing Modifiers etc.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_air_pnr_element: None | AddAirPnrElement = field(
        default=None,
        metadata={
            "name": "AddAirPnrElement",
            "type": "Element",
        },
    )
    update_air_pnr_element: None | UpdateAirPnrElement = field(
        default=None,
        metadata={
            "name": "UpdateAirPnrElement",
            "type": "Element",
        },
    )
    delete_air_pnr_element: None | DeleteAirPnrElement = field(
        default=None,
        metadata={
            "name": "DeleteAirPnrElement",
            "type": "Element",
        },
    )
