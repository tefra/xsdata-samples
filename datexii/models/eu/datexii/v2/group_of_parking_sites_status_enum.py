from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class GroupOfParkingSitesStatusEnum(Enum):
    """
    The status of the group of parking sites (available spaces or not).

    :cvar ALL_PARKINGS_FULL: All parkings within the group are full.
    :cvar MULTI_STOREY_PARKINGS_FULL: All multi storey parkings within
        the group are full.
    :cvar NO_MORE_PARKING_SPACES_AVAILABLE: No more parking spaces
        available within the group.
    :cvar ENOUGH_SPACES_AVAILABLE: Enough spaces available within the
        group.
    :cvar UNKNOWN: The status of the group of parking sites is unknown.
    :cvar OTHER: Other.
    """
    ALL_PARKINGS_FULL = "allParkingsFull"
    MULTI_STOREY_PARKINGS_FULL = "multiStoreyParkingsFull"
    NO_MORE_PARKING_SPACES_AVAILABLE = "noMoreParkingSpacesAvailable"
    ENOUGH_SPACES_AVAILABLE = "enoughSpacesAvailable"
    UNKNOWN = "unknown"
    OTHER = "other"
