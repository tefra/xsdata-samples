from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class CarParkConfigurationEnum(Enum):
    """
    Types of configuration/layout of a car park.

    :cvar MULTI_STOREY: Parking is on multiple levels within a car park
        building.
    :cvar PARK_AND_RIDE: Car parking facility is associated with a park
        and ride service.
    :cvar SINGLE_LEVEL: Parking is on a single ground floor level.
    :cvar UNDERGROUND: Parking is on one or more floors below ground
        level.
    """

    MULTI_STOREY = "multiStorey"
    PARK_AND_RIDE = "parkAndRide"
    SINGLE_LEVEL = "singleLevel"
    UNDERGROUND = "underground"
