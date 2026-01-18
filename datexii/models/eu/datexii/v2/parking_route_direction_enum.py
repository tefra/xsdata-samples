from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingRouteDirectionEnum(Enum):
    """
    The direction of the parking route.

    :cvar TOWARDS_PARKING_SITE: Towards parking site.
    :cvar AWAY_FROM_PARKING_SITE: Away from parking site.
    """

    TOWARDS_PARKING_SITE = "towardsParkingSite"
    AWAY_FROM_PARKING_SITE = "awayFromParkingSite"
