from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VehicleStatusEnum(Enum):
    """
    The status of a vehicle.

    :cvar ABANDONED: Abandoned vehicle.
    :cvar BROKEN_DOWN: Broken down vehicle (i.e. it is immobile due to
        mechanical breakdown).
    :cvar BURNT_OUT: Burnt out vehicle, but fire is extinguished.
    :cvar DAMAGED: Vehicle is damaged following an incident or
        collision. It may or may not be able to move by itself.
    :cvar DAMAGED_AND_IMMOBILIZED: Vehicle is damaged following an
        incident or collision. It is immobilized and therefore needs
        assistance to be moved.
    :cvar ON_FIRE: Vehicle is on fire.
    """

    ABANDONED = "abandoned"
    BROKEN_DOWN = "brokenDown"
    BURNT_OUT = "burntOut"
    DAMAGED = "damaged"
    DAMAGED_AND_IMMOBILIZED = "damagedAndImmobilized"
    ON_FIRE = "onFire"
