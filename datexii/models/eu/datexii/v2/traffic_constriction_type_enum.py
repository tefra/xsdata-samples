from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TrafficConstrictionTypeEnum(Enum):
    """
    Types of constriction to which traffic is subjected as a result of an
    event.

    :cvar CARRIAGEWAY_BLOCKED: The carriageway is totally obstructed in
        the specified direction due to an unplanned event.
    :cvar CARRIAGEWAY_PARTIALLY_OBSTRUCTED: The carriageway is partially
        obstructed in the specified direction due to an unplanned event.
    :cvar LANES_BLOCKED: One or more lanes is totally obstructed in the
        specified direction due to an unplanned event.
    :cvar LANES_PARTIALLY_OBSTRUCTED: One or more lanes is partially
        obstructed in the specified direction due to an unplanned event.
    :cvar ROAD_BLOCKED: The road is totally obstructed, for all vehicles
        in both directions, due to an unplanned event.
    :cvar ROAD_PARTIALLY_OBSTRUCTED: The road is partially obstructed in
        both directions due to an unplanned event.
    """

    CARRIAGEWAY_BLOCKED = "carriagewayBlocked"
    CARRIAGEWAY_PARTIALLY_OBSTRUCTED = "carriagewayPartiallyObstructed"
    LANES_BLOCKED = "lanesBlocked"
    LANES_PARTIALLY_OBSTRUCTED = "lanesPartiallyObstructed"
    ROAD_BLOCKED = "roadBlocked"
    ROAD_PARTIALLY_OBSTRUCTED = "roadPartiallyObstructed"
