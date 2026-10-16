from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypePosition(StrEnum):
    """
    Facility position with respect to position within the aircraft cabin.

    Possible values are – Left, Right, Center, Left Center, Right Center.
    """

    LEFT = "Left"
    RIGHT = "Right"
    CENTER = "Center"
    LEFT_CENTER = "LeftCenter"
    RIGHT_CENTER = "RightCenter"
