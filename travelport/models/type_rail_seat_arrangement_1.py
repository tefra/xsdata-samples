from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeRailSeatArrangement1(Enum):
    """
    The type of Rail Seat Arrangement.
    """

    POWER_PLUG = "Power Plug"
    SUITABLE_FOR_PETS = "Suitable for Pets"
    WITH_MOBILE_PHONE = "With Mobile Phone"
    SOLO_ISOLATED_SEAT = "Solo Isolated Seat"
