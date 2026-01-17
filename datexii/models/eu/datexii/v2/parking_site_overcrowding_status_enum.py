from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingSiteOvercrowdingStatusEnum(Enum):
    """
    The overcrowding status of the parking site.

    Choose between two levels or simply (no) overcrowding.

    :cvar OVERCROWDING: The parking site is overcrowded (as specified in
        ParkingThresholds).
    :cvar NO_OVERCROWDING: The parking site is not overcrowded.
    :cvar OVERCROWDING_LEVEL1: The parking site is overcrowded at level
        1 (as specified in ParkingThresholds).
    :cvar OVERCROWDING_LEVEL2: The parking site is overcrowded at level
        2 (as specified in ParkingThresholds).
    :cvar UNKNOWN: The overcrowding level is unknown.
    :cvar OTHER: Other.
    """

    OVERCROWDING = "overcrowding"
    NO_OVERCROWDING = "noOvercrowding"
    OVERCROWDING_LEVEL1 = "overcrowdingLevel1"
    OVERCROWDING_LEVEL2 = "overcrowdingLevel2"
    UNKNOWN = "unknown"
    OTHER = "other"
