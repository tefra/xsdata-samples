from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc01AreaLocationSubtypeEnum(Enum):
    """
    Types of area.

    :cvar LARGE_AREA: A geographic or geometric large area.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    LARGE_AREA = "largeArea"
    OTHER = "other"
