from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class ArvlUnknSegment:
    """
    An ARNK segment that identifies a missing travel information.

    Parameters
    ----------
    booking_traveler_ref
        Reference Element for Booking Traveler
    key
    origin
        The IATA CITY code for this origination of this entity.
    destination
        The IATA CITY code for this destination of this entity.
    travel_order
        To identify the appropriate travel sequence for Air/Car/Hotel
        segments/reservations based on travel dates. This ordering is
        applicable across the UR not provider or traveler specific
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    booking_traveler_ref: list[ArvlUnknSegment.BookingTravelerRef] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 255,
        },
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    travel_order: None | int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class BookingTravelerRef:
        key: str = field(
            metadata={
                "name": "Key",
                "type": "Attribute",
                "required": True,
            }
        )
