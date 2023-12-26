from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticClearEventAllowedBehaviorEnumSimple(Enum):
    """
    :cvar NO_STATUS_BYTE_CHANGE: The event status byte keeps unchanged.
    :cvar ONLY_THIS_CYCLE_AND_READINESS: The OperationCycle and
        readiness bits of the event status byte are reset.
    """

    NO_STATUS_BYTE_CHANGE = "NO-STATUS-BYTE-CHANGE"
    ONLY_THIS_CYCLE_AND_READINESS = "ONLY-THIS-CYCLE-AND-READINESS"
