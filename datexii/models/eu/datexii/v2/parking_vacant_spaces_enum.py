from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingVacantSpacesEnum(Enum):
    """
    Parking vacant spaces enum.

    :cvar NO_PARKING_SPACES_AVAILABLE: No parking spaces available.
    :cvar EXPECT_NO_SPACES_AVAILABLE: Expect no parking spaces
        available.
    :cvar ONLY_AFEW_SPACES_AVAILABLE: Only a few parking spaces
        available.
    :cvar LESS_THAN10_SPACES_AVAILABLE: Less than 10 parking spaces
        available.
    :cvar LESS_THAN20_SPACES_AVAILABLE: Less than 20 parking spaces
        available.
    :cvar LESS_THAN30_SPACES_AVAILABLE: Less than 30 parking spaces
        available.
    :cvar LESS_THAN40_SPACES_AVAILABLE: Less than 40 parking spaces
        available.
    :cvar LESS_THAN50_SPACES_AVAILABLE: Less than 50 parking spaces
        available.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """

    NO_PARKING_SPACES_AVAILABLE = "noParkingSpacesAvailable"
    EXPECT_NO_SPACES_AVAILABLE = "expectNoSpacesAvailable"
    ONLY_AFEW_SPACES_AVAILABLE = "onlyAFewSpacesAvailable"
    LESS_THAN10_SPACES_AVAILABLE = "lessThan10SpacesAvailable"
    LESS_THAN20_SPACES_AVAILABLE = "lessThan20SpacesAvailable"
    LESS_THAN30_SPACES_AVAILABLE = "lessThan30SpacesAvailable"
    LESS_THAN40_SPACES_AVAILABLE = "lessThan40SpacesAvailable"
    LESS_THAN50_SPACES_AVAILABLE = "lessThan50SpacesAvailable"
    UNKNOWN = "unknown"
    OTHER = "other"
