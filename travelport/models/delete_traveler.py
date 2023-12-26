from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_booking_traveler_element import (
    TypeBookingTravelerElement,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class DeleteTraveler:
    """
    Container for Booking Traveler or its contents to be deleted.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    element: None | TypeBookingTravelerElement = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Attribute",
            "required": True,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
