from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingOccupancyTrendEnum(Enum):
    """
    List of terms used to describe the trend in parking space occupancy.

    :cvar DECREASING: Parking space occupancy is decreasing.
    :cvar INCREASING: Parking space occupancy is increasing.
    :cvar STABLE: Parking space occupancy is stable.
    :cvar INCREASING_QUICKLY: Parking space occupancy is increasing
        quickly.
    :cvar INCREASING_SLOWLY: Parking space occupancy is increasing
        slowly.
    :cvar DECREASING_QUICKLY: Parking space occupancy is decreasing
        quickly.
    :cvar DECREASING_SLOWLY: Parking space occupancy is decreasing
        slowly.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """

    DECREASING = "decreasing"
    INCREASING = "increasing"
    STABLE = "stable"
    INCREASING_QUICKLY = "increasingQuickly"
    INCREASING_SLOWLY = "increasingSlowly"
    DECREASING_QUICKLY = "decreasingQuickly"
    DECREASING_SLOWLY = "decreasingSlowly"
    UNKNOWN = "unknown"
    OTHER = "other"
