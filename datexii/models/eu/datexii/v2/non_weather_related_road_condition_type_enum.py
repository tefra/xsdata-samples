from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class NonWeatherRelatedRoadConditionTypeEnum(Enum):
    """
    Types of road surface conditions which are not related to the weather.

    :cvar DIESEL_ON_ROAD: Increased skid risk due to diesel on the road.
    :cvar LEAVES_ON_ROAD: Increased skid risk due to leaves on road.
    :cvar LOOSE_CHIPPINGS: Increased skid risk and injury risk due to
        loose chippings on road.
    :cvar LOOSE_SAND_ON_ROAD: Increased skid risk due to loose sand on
        road.
    :cvar MUD_ON_ROAD: Increased skid risk due to mud on road.
    :cvar OIL_ON_ROAD: Increased skid risk due to oil on road.
    :cvar PETROL_ON_ROAD: Increased skid risk due to petrol on road.
    :cvar ROAD_SURFACE_IN_POOR_CONDITION: The road surface is damaged,
        severely rutted or potholed (i.e. it is in a poor state of
        repair).
    :cvar SLIPPERY_ROAD: The road surface is slippery due to an
        unspecified non-weather related cause.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    DIESEL_ON_ROAD = "dieselOnRoad"
    LEAVES_ON_ROAD = "leavesOnRoad"
    LOOSE_CHIPPINGS = "looseChippings"
    LOOSE_SAND_ON_ROAD = "looseSandOnRoad"
    MUD_ON_ROAD = "mudOnRoad"
    OIL_ON_ROAD = "oilOnRoad"
    PETROL_ON_ROAD = "petrolOnRoad"
    ROAD_SURFACE_IN_POOR_CONDITION = "roadSurfaceInPoorCondition"
    SLIPPERY_ROAD = "slipperyRoad"
    OTHER = "other"
