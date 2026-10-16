from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeDoorCount(StrEnum):
    TWO_TO_THREE_DOORS = "TwoToThreeDoors"
    TWO_TO_FOUR_DOORS = "TwoToFourDoors"
    FOUR_TO_FIVE_DOORS = "FourToFiveDoors"
