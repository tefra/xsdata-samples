from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_booking_traveler_element import (
    TypeBookingTravelerElement,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass(kw_only=True)
class DeleteTraveler:
    """
    Container for Booking Traveler or its contents to be deleted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    element: TypeBookingTravelerElement = field(
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
