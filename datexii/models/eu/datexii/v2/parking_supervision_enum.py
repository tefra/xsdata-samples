from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingSupervisionEnum(Enum):
    """
    Defines the kind of supervision of the parking site.

    :cvar REMOTE: Remote.
    :cvar ON_SITE: On site.
    :cvar CONTROL_CENTRE_ON_SITE: Control centre on site.
    :cvar CONTROL_CENTRE_OFF_SITE: Control centre off site.
    :cvar PATROL: Patrol.
    :cvar NONE: None.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """

    REMOTE = "remote"
    ON_SITE = "onSite"
    CONTROL_CENTRE_ON_SITE = "controlCentreOnSite"
    CONTROL_CENTRE_OFF_SITE = "controlCentreOffSite"
    PATROL = "patrol"
    NONE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"
