from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AccessCategoryEnum(Enum):
    """
    Specifies the category of the access.

    :cvar VEHICLE_ENTRANCE_AND_EXIT: An entrance and exit for vehicles.
    :cvar VEHICLE_ENTRANCE: An entrance for vehicles.
    :cvar VEHICLE_EXIT: An exit for vehicles.
    :cvar PEDESTRIAN_ENTRANCE_AND_EXIT: An entrance and exit for
        pedestrian.
    :cvar PEDESTRIAN_ENTRANCE: An entrance for pedestrian.
    :cvar PEDESTRIAN_EXIT: An exit for pedestrian.
    :cvar RENTAL_CAR_RETURN: An entrance to return rental cars.
    :cvar BICYCLES: An access for bicycles.
    :cvar EMERGENCY_EXIT: An exit that can be used by pedestrians in
        case of emergency (i.e. among others easy to access and signed).
    :cvar UNSPECIFIED: The category of this access is not specified any
        further.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """

    VEHICLE_ENTRANCE_AND_EXIT = "vehicleEntranceAndExit"
    VEHICLE_ENTRANCE = "vehicleEntrance"
    VEHICLE_EXIT = "vehicleExit"
    PEDESTRIAN_ENTRANCE_AND_EXIT = "pedestrianEntranceAndExit"
    PEDESTRIAN_ENTRANCE = "pedestrianEntrance"
    PEDESTRIAN_EXIT = "pedestrianExit"
    RENTAL_CAR_RETURN = "rentalCarReturn"
    BICYCLES = "bicycles"
    EMERGENCY_EXIT = "emergencyExit"
    UNSPECIFIED = "unspecified"
    UNKNOWN = "unknown"
    OTHER = "other"
