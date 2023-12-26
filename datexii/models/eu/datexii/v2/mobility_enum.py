from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class MobilityEnum(Enum):
    """
    Types of mobility relating to a situation element defined by a SituationReord.

    :cvar MOBILE: The described element of a situation is moving.
    :cvar STATIONARY: The described element of a situation is
        stationary.
    :cvar UNKNOWN: The mobility of the described element of a situation
        is unknown.
    """

    MOBILE = "mobile"
    STATIONARY = "stationary"
    UNKNOWN = "unknown"
