from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticSignificanceEnumSimple(Enum):
    """
    :cvar FAULT: Failure, which affects the component/ECU itself.
    :cvar OCCURENCE: Issue, which indicates additional information
        concerning insufficient system behavior.
    """
    FAULT = "FAULT"
    OCCURENCE = "OCCURENCE"
