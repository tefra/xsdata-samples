from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticTypeOfFreezeFrameRecordNumerationEnumSimple(Enum):
    """
    :cvar CALCULATED: Freeze frame records will be numbered consecutive
        starting by 1 in their chronological order.
    :cvar CONFIGURED: Freeze frame records will be numbered based on the
        given configuration in their chronological order.
    """

    CALCULATED = "CALCULATED"
    CONFIGURED = "CONFIGURED"
