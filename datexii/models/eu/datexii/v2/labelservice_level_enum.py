from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LABELServiceLevelEnum(Enum):
    """Service level defined by the LABEL project http://truckparkinglabel.eu.

    :cvar NONE: None.
    :cvar SERVICE_LEVEL1: Providing the basics.
    :cvar SERVICE_LEVEL2: Also providing washing facilities and a more
        convenient lay-out of the parking area.
    :cvar SERVICE_LEVEL3: Providing service for personal hygiene and
        shop/ fuel station.
    :cvar SERVICE_LEVEL4: Providing full service for driver and vehicle.
    :cvar SERVICE_LEVEL5: Providing the high end of comfort levels.
    :cvar UNKNOWN: Unknown.
    """

    NONE = "none"
    SERVICE_LEVEL1 = "serviceLevel1"
    SERVICE_LEVEL2 = "serviceLevel2"
    SERVICE_LEVEL3 = "serviceLevel3"
    SERVICE_LEVEL4 = "serviceLevel4"
    SERVICE_LEVEL5 = "serviceLevel5"
    UNKNOWN = "unknown"
