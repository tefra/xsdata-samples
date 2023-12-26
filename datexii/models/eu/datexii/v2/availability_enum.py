from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AvailabilityEnum(Enum):
    """
    An enumeration which states if something is available or not.

    :cvar AVAILABLE: The element in question is available.
    :cvar NOT_AVAILABLE: The element in question is not available.
    :cvar UNKNOWN: There is no information about whether the element in
        question is available or not.
    """

    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
    UNKNOWN = "unknown"
