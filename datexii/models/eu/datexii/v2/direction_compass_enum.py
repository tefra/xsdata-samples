from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class DirectionCompassEnum(Enum):
    """
    Cardinal direction points of the compass.

    :cvar EAST: East.
    :cvar EAST_NORTH_EAST: East north east.
    :cvar EAST_SOUTH_EAST: East south east.
    :cvar NORTH: North.
    :cvar NORTH_EAST: North east.
    :cvar NORTH_NORTH_EAST: North north east.
    :cvar NORTH_NORTH_WEST: North north west.
    :cvar NORTH_WEST: North west.
    :cvar SOUTH: South.
    :cvar SOUTH_EAST: South east.
    :cvar SOUTH_SOUTH_EAST: South south east.
    :cvar SOUTH_SOUTH_WEST: South south west.
    :cvar SOUTH_WEST: South west.
    :cvar WEST: West.
    :cvar WEST_NORTH_WEST: West north west.
    :cvar WEST_SOUTH_WEST: West south west.
    """

    EAST = "east"
    EAST_NORTH_EAST = "eastNorthEast"
    EAST_SOUTH_EAST = "eastSouthEast"
    NORTH = "north"
    NORTH_EAST = "northEast"
    NORTH_NORTH_EAST = "northNorthEast"
    NORTH_NORTH_WEST = "northNorthWest"
    NORTH_WEST = "northWest"
    SOUTH = "south"
    SOUTH_EAST = "southEast"
    SOUTH_SOUTH_EAST = "southSouthEast"
    SOUTH_SOUTH_WEST = "southSouthWest"
    SOUTH_WEST = "southWest"
    WEST = "west"
    WEST_NORTH_WEST = "westNorthWest"
    WEST_SOUTH_WEST = "westSouthWest"
