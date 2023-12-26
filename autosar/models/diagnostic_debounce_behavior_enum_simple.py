from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticDebounceBehaviorEnumSimple(Enum):
    """
    :cvar FREEZE: The event debounce counter will be frozen with the
        current value and will not change while a related enable
        condition is not fulfilled or ControlDTCSetting of the related
        event is disabled. After all related enable conditions are
        fulfilled and ControlDTCSetting of the related event is enabled
        again, the event qualification will continue with the next
        report of the event (i.e. SetEventStatus).
    :cvar RESET: The event debounce counter will be reset to initial
        value if a related enable condition is not fulfilled or
        ControlDTCSetting of the related event is disabled. The
        qualification of the event will be restarted with the next valid
        event report.
    """

    FREEZE = "FREEZE"
    RESET = "RESET"
