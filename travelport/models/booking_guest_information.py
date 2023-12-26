from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_guest_room_information import (
    TypeGuestRoomInformation,
)

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class BookingGuestInformation:
    """
    Information about requested rooms and guests allocation.

    Parameters
    ----------
    room
        Individual room. Multiple occurrences if there are multiple rooms in
        the request. Maximum number of rooms may vary by supplier or
        aggregator.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    room: list[TypeGuestRoomInformation] = field(
        default_factory=list,
        metadata={
            "name": "Room",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )
