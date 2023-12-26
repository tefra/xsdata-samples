from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OpenlrOrientationEnum(Enum):
    """
    Enumeration of side of road.

    :cvar NO_ORIENTATION_OR_UNKNOWN: No orientation or unknown
    :cvar WITH_LINE_DIRECTION: With line direction
    :cvar AGAINST_LINE_DIRECTION: Against line direction
    :cvar BOTH: Both directions
    """

    NO_ORIENTATION_OR_UNKNOWN = "noOrientationOrUnknown"
    WITH_LINE_DIRECTION = "withLineDirection"
    AGAINST_LINE_DIRECTION = "againstLineDirection"
    BOTH = "both"
