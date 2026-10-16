from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class TypeProduct2(StrEnum):
    """
    Available product types.
    """

    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    CRUISE = "Cruise"
    OTHER = "Other"
