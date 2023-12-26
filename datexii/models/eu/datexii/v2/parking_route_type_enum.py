from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingRouteTypeEnum(Enum):
    """
    The type of the parking route.

    :cvar PEDESTRIAN: A parking route for pedestrian.
    :cvar BICYCLE: A parking route for bicycles.
    :cvar LORRY: A parking route for lorries.
    :cvar OTHER: Another type of parking route.
    """

    PEDESTRIAN = "pedestrian"
    BICYCLE = "bicycle"
    LORRY = "lorry"
    OTHER = "other"
