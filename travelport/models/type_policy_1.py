from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypePolicy1(Enum):
    """
    Available product types.
    """
    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    TICKETING = "Ticketing"
