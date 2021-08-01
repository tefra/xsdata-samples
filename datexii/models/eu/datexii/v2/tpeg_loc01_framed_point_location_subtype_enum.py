from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc01FramedPointLocationSubtypeEnum(Enum):
    """
    Types of points on the road network framed by two other points on the same
    road.

    :cvar FRAMED_POINT: A point on the road network framed by two other
        points on the same road.
    """
    FRAMED_POINT = "framedPoint"
