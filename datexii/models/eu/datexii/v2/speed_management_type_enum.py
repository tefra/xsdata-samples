from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class SpeedManagementTypeEnum(Enum):
    """
    Management actions relating to speed.

    :cvar ACTIVE_SPEED_CONTROL_IN_OPERATION: Automatic speed control
        measures are in place at the specified location, whereby speed
        limits are set by an automatic system which is triggered by
        traffic sensing equipment.
    :cvar DO_NOT_SLOWDOWN_UNNECESSARILY: Do not slow down unnecessarily.
    :cvar OBSERVE_SPEED_LIMIT: Observe speed limit.
    :cvar POLICE_SPEED_CHECKS_IN_OPERATION: Police speed checks are in
        operation.
    :cvar REDUCE_YOUR_SPEED: Reduce your speed.
    :cvar SPEED_RESTRICTION_IN_OPERATION: A speed restriction is in
        operation.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    ACTIVE_SPEED_CONTROL_IN_OPERATION = "activeSpeedControlInOperation"
    DO_NOT_SLOWDOWN_UNNECESSARILY = "doNotSlowdownUnnecessarily"
    OBSERVE_SPEED_LIMIT = "observeSpeedLimit"
    POLICE_SPEED_CHECKS_IN_OPERATION = "policeSpeedChecksInOperation"
    REDUCE_YOUR_SPEED = "reduceYourSpeed"
    SPEED_RESTRICTION_IN_OPERATION = "speedRestrictionInOperation"
    OTHER = "other"
