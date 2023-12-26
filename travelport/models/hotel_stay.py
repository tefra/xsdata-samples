from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelStay:
    """
    Arrival and Departure dates.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    checkin_date: None | str = field(
        default=None,
        metadata={
            "name": "CheckinDate",
            "type": "Element",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    checkout_date: None | str = field(
        default=None,
        metadata={
            "name": "CheckoutDate",
            "type": "Element",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
