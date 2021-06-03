from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticRoutineTypeEnumSimple(Enum):
    """
    :cvar ASYNCHRONOUS: This indicates that the diagnostic server is not
        blocked while the diagnostic routine is running.
    :cvar SYNCHRONOUS: This indicates that the diagnostic routine blocks
        the diagnostic server in the ECU while the routine is running.
    """
    ASYNCHRONOUS = "ASYNCHRONOUS"
    SYNCHRONOUS = "SYNCHRONOUS"
