from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OpenlrSideOfRoadEnum(StrEnum):
    """
    Enumeration of side of road.

    :cvar ON_ROAD_OR_UNKNOWN: On road or unknown
    :cvar RIGHT: right
    :cvar LEFT: left
    :cvar BOTH: both
    """

    ON_ROAD_OR_UNKNOWN = "onRoadOrUnknown"
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"
