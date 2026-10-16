from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeRailSeating2(StrEnum):
    """
    The type of Rail Seating.
    """

    CAR_PARKING = "Car-Parking"
    MOTORRAIL = "Motorrail"
    SEAT_COUCHETTE = "Seat Couchette"
    SLEEPER = "Sleeper"
