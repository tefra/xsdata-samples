from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RoadTypeEnum(Enum):
    """
    Categorisation of the  road type (motorway, main road, ...).

    :cvar MOTORWAY: Motorway.
    :cvar TRUNK_ROAD: Trunk road.
    :cvar MAIN_ROAD: Main road.
    :cvar OTHER: Other.
    """
    MOTORWAY = "motorway"
    TRUNK_ROAD = "trunkRoad"
    MAIN_ROAD = "mainRoad"
    OTHER = "other"
