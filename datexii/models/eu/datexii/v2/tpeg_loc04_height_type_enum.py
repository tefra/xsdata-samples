from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TpegLoc04HeightTypeEnum(Enum):
    """
    Types of height.

    :cvar ABOVE: Height above specified location.
    :cvar ABOVE_SEA_LEVEL: Height above mean sea high water level.
    :cvar ABOVE_STREET_LEVEL: Height above street level.
    :cvar AT: At height of specified location.
    :cvar AT_SEA_LEVEL: At mean sea high water level.
    :cvar AT_STREET_LEVEL: At street level.
    :cvar BELOW: Height below specified location.
    :cvar BELOW_SEA_LEVEL: Height below mean sea high water level.
    :cvar BELOW_STREET_LEVEL: Height below street level.
    :cvar UNDEFINED: Undefined height reference.
    :cvar UNKNOWN: Unknown height reference.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ABOVE = "above"
    ABOVE_SEA_LEVEL = "aboveSeaLevel"
    ABOVE_STREET_LEVEL = "aboveStreetLevel"
    AT = "at"
    AT_SEA_LEVEL = "atSeaLevel"
    AT_STREET_LEVEL = "atStreetLevel"
    BELOW = "below"
    BELOW_SEA_LEVEL = "belowSeaLevel"
    BELOW_STREET_LEVEL = "belowStreetLevel"
    UNDEFINED = "undefined"
    UNKNOWN = "unknown"
    OTHER = "other"
