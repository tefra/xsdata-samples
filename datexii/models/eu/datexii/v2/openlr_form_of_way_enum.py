from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OpenlrFormOfWayEnum(Enum):
    """
    Enumeration of for of way.

    :cvar UNDEFINED: undefined
    :cvar MOTORWAY: motorway
    :cvar MULTIPLE_CARRIAGEWAY: multipleCarrigeway
    :cvar SINGLE_CARRIAGEWAY: single carrigeway
    :cvar ROUNDABOUT: roadabout
    :cvar SLIP_ROAD: sliproad
    :cvar TRAFFIC_SQUARE: traffic square
    :cvar OTHER: other
    """

    UNDEFINED = "undefined"
    MOTORWAY = "motorway"
    MULTIPLE_CARRIAGEWAY = "multipleCarriageway"
    SINGLE_CARRIAGEWAY = "singleCarriageway"
    ROUNDABOUT = "roundabout"
    SLIP_ROAD = "slipRoad"
    TRAFFIC_SQUARE = "trafficSquare"
    OTHER = "other"
