from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeRailSeating1(Enum):
    """
    The type of Rail Seating.
    """

    CAR_PARKING = "Car-Parking"
    MOTORRAIL = "Motorrail"
    SEAT_COUCHETTE = "Seat Couchette"
    SLEEPER = "Sleeper"
