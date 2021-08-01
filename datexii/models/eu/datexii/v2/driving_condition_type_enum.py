from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class DrivingConditionTypeEnum(Enum):
    """
    Types of the perceived driving conditions.

    :cvar IMPOSSIBLE: Current conditions are making driving impossible.
    :cvar HAZARDOUS: Driving conditions are hazardous due to
        environmental conditions.
    :cvar NORMAL: Driving conditions are normal.
    :cvar PASSABLE_WITH_CARE: The roadway is passable to vehicles with
        driver care.
    :cvar UNKNOWN: Driving conditions are unknown.
    :cvar VERY_HAZARDOUS: Driving conditions are very hazardous due to
        environmental conditions.
    :cvar WINTER_CONDITIONS: Driving conditions are consistent with
        those expected in winter.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    IMPOSSIBLE = "impossible"
    HAZARDOUS = "hazardous"
    NORMAL = "normal"
    PASSABLE_WITH_CARE = "passableWithCare"
    UNKNOWN = "unknown"
    VERY_HAZARDOUS = "veryHazardous"
    WINTER_CONDITIONS = "winterConditions"
    OTHER = "other"
