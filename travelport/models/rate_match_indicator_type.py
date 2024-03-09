from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class RateMatchIndicatorType(Enum):
    RATE_CATEGORY = "RateCategory"
    ROOM_COUNT = "RoomCount"
    ADULT_COUNT = "AdultCount"
    CHILD_COUNT = "ChildCount"
    ADULT_ROLLAWAY = "AdultRollaway"
    CHILD_ROLLAWAY = "ChildRollaway"
    CRIB = "Crib"
