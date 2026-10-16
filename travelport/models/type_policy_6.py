from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


class TypePolicy6(StrEnum):
    """
    Available product types.
    """

    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    TICKETING = "Ticketing"
