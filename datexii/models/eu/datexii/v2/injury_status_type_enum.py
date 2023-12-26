from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class InjuryStatusTypeEnum(Enum):
    """
    Types of injury status of people.

    :cvar DEAD: Dead.
    :cvar INJURED: Injured requiring medical treatment.
    :cvar SERIOUSLY_INJURED: Seriously injured requiring urgent hospital
        treatment.
    :cvar SLIGHTLY_INJURED: Slightly injured requiring medical
        treatment.
    :cvar UNINJURED: Uninjured.
    :cvar UNKNOWN: Injury status unknown.
    """

    DEAD = "dead"
    INJURED = "injured"
    SERIOUSLY_INJURED = "seriouslyInjured"
    SLIGHTLY_INJURED = "slightlyInjured"
    UNINJURED = "uninjured"
    UNKNOWN = "unknown"
