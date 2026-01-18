from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingSiteStatusEnum(Enum):
    """
    The status of the parking site (spaces available or not).

    :cvar SPACES_AVAILABLE: Parking spaces are currently available.
    :cvar ALMOST_FULL: The parking site is almost full (as defined by
        its configuration parameters).
    :cvar FULL_AT_ENTRANCE: The parking site is considered full at its
        entrance (e.g. full sign is displayed at entrance or on managing
        VMS).
    :cvar FULL: The parking site is full (as defined by its
        configuration parameters).
    :cvar UNKNOWN: The status of the parking site is unknown.
    :cvar OTHER: Other.
    """

    SPACES_AVAILABLE = "spacesAvailable"
    ALMOST_FULL = "almostFull"
    FULL_AT_ENTRANCE = "fullAtEntrance"
    FULL = "full"
    UNKNOWN = "unknown"
    OTHER = "other"
