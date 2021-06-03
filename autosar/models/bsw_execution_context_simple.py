from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class BswExecutionContextSimple(Enum):
    """
    :cvar HOOK: Context of an OS "hook" routine always
    :cvar INTERRUPT_CAT_1: CAT1 interrupt context always
    :cvar INTERRUPT_CAT_2: CAT2 interrupt context always
    :cvar TASK: Task context always
    :cvar UNSPECIFIED: The execution context is not specified by the API
    """
    HOOK = "HOOK"
    INTERRUPT_CAT_1 = "INTERRUPT-CAT-1"
    INTERRUPT_CAT_2 = "INTERRUPT-CAT-2"
    TASK = "TASK"
    UNSPECIFIED = "UNSPECIFIED"
