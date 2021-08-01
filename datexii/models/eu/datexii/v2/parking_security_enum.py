from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingSecurityEnum(Enum):
    """
    Specifies security measures related to the parking site or particular
    spaces.

    :cvar SOCIAL_CONTROL: Social control e.g. parking situated in a
        neighbourhood.
    :cvar SECURITY_STAFF: Security staff.
    :cvar EXTERNAL_SECURITY: External security, e.g. police or staff not
        directly belonging to the parking.
    :cvar CCTV: CCTV (camera observation).
    :cvar DOG: Dog.
    :cvar GUARD24HOURS: 24/24 guard.
    :cvar LIGHTING: Site is illuminated in a normal way (but not as
        strong as 'floodLight').
    :cvar FLOOD_LIGHT: Flood light (stronger than lighting).
    :cvar FENCES: Fences.
    :cvar AREA_SEPERATED_FROM_SURROUNDINGS: Site is separated from its
        surroundings. Can also be used to express a space for noise-
        producing vehicles, e.g. lorries with cooling generators.
    :cvar NONE: There are no security measures.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: None of the values in this enumeration applies. Use
        'parkingAdditionalSecurity' instead.
    """
    SOCIAL_CONTROL = "socialControl"
    SECURITY_STAFF = "securityStaff"
    EXTERNAL_SECURITY = "externalSecurity"
    CCTV = "cctv"
    DOG = "dog"
    GUARD24HOURS = "guard24hours"
    LIGHTING = "lighting"
    FLOOD_LIGHT = "floodLight"
    FENCES = "fences"
    AREA_SEPERATED_FROM_SURROUNDINGS = "areaSeperatedFromSurroundings"
    NONE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"
