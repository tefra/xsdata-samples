from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class HandleTerminationAndRestartEnumSimple(Enum):
    """
    :cvar CAN_BE_TERMINATED: Supports termination.
    :cvar CAN_BE_TERMINATED_AND_RESTARTED: Supports termination and
        restarting.
    :cvar NO_SUPPORT: Stop and restart is not supported at all.
    """
    CAN_BE_TERMINATED = "CAN-BE-TERMINATED"
    CAN_BE_TERMINATED_AND_RESTARTED = "CAN-BE-TERMINATED-AND-RESTARTED"
    NO_SUPPORT = "NO-SUPPORT"
