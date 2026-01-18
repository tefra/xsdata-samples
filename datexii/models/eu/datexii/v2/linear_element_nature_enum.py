from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LinearElementNatureEnum(Enum):
    """
    List of indicative natures of linear elements.

    :cvar ROAD: The nature of the linear element is a road.
    :cvar ROAD_SECTION: The nature of the linear element is a section of
        a road.
    :cvar SLIP_ROAD: The nature of the linear element is a slip road.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    ROAD = "road"
    ROAD_SECTION = "roadSection"
    SLIP_ROAD = "slipRoad"
    OTHER = "other"
