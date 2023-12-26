from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LABELSecurityLevelEnum(Enum):
    """Security level defined by the LABEL project http://truckparkinglabel.eu.

    :cvar NONE: None.
    :cvar SECURITY_LEVEL1: Providing the basics.
    :cvar SECURITY_LEVEL2: Technical measures to improve security.
    :cvar SECURITY_LEVEL3: Security measures are combined, Access of
        persons restricted.
    :cvar SECURITY_LEVEL4: Real time monitoring of vehicles and persons
        by professional staff.
    :cvar SECURITY_LEVEL5: Verification of vehicles and persons by
        professional staff, site manned around the clock.
    :cvar UNKNOWN: Unknown.
    """

    NONE = "none"
    SECURITY_LEVEL1 = "securityLevel1"
    SECURITY_LEVEL2 = "securityLevel2"
    SECURITY_LEVEL3 = "securityLevel3"
    SECURITY_LEVEL4 = "securityLevel4"
    SECURITY_LEVEL5 = "securityLevel5"
    UNKNOWN = "unknown"
