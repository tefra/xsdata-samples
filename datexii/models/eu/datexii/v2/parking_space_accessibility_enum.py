from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingSpaceAccessibilityEnum(Enum):
    """
    Easements for handicapped people expecially related to a parking space or a
    group of parking spaces.

    :cvar EXTRA_SPACE_LEFT_SIDE: There is some extra space on the left
        side of the parking space (in parking direction point of view),
        for example to improve the situation for wheelchair users.
    :cvar EXTRA_SPACE_RIGHT_SIDE: There is some extra space on the right
        side of the parking space (in parking direction point of view),
        for example to improve the situation for wheelchair users.
    :cvar NEARBY_PEDESTRIAN_EXIT: The parking space is quite near to a
        pedestrian exit. Note: Can be more exactly defined by using
        'dedicatedAccess'.
    :cvar BORDERS_MARKED: The border of the parking space is marked
        (painted on the ground).
    :cvar OTHER: Other.
    """
    EXTRA_SPACE_LEFT_SIDE = "extraSpaceLeftSide"
    EXTRA_SPACE_RIGHT_SIDE = "extraSpaceRightSide"
    NEARBY_PEDESTRIAN_EXIT = "nearbyPedestrianExit"
    BORDERS_MARKED = "bordersMarked"
    OTHER = "other"
