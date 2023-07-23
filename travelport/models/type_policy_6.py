from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


class TypePolicy6(Enum):
    """
    Available product types.
    """
    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    TICKETING = "Ticketing"
