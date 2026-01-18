from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_hotel_pnr_element import TypeHotelPnrElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class DeleteHotelPnrElement:
    """
    Container for Hotel PNR elements to be deleted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    reservation_locator_code: str = field(
        metadata={
            "name": "ReservationLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    element: TypeHotelPnrElement = field(
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        }
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
