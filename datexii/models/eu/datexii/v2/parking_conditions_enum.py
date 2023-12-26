from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingConditionsEnum(Enum):
    """
    Defines if normal parking conditions are suspended or special parking
    conditions are in force.

    :cvar NORMAL_PARKING_CONDITIONS_SUSPENDED: The parking conditions
        (possibly including tariffs) that normally apply are temporarily
        suspended.
    :cvar SPECIAL_PARKING_CONDITIONS_IN_FORCE: Parking conditions, other
        than those that normally apply, are currently in force for the
        parking site.
    :cvar OTHER: Other.
    """

    NORMAL_PARKING_CONDITIONS_SUSPENDED = "normalParkingConditionsSuspended"
    SPECIAL_PARKING_CONDITIONS_IN_FORCE = "specialParkingConditionsInForce"
    OTHER = "other"
