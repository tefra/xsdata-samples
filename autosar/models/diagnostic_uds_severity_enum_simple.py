from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticUdsSeverityEnumSimple(Enum):
    """
    :cvar CHECK_AT_NEXT_HALT: Check at next halt.
    :cvar IMMEDIATELY: Check immediately.
    :cvar MAINTENANCE_ONLY: Maintenance required.
    :cvar NO_SEVERITY: No severity information available.
    """
    CHECK_AT_NEXT_HALT = "CHECK-AT-NEXT-HALT"
    IMMEDIATELY = "IMMEDIATELY"
    MAINTENANCE_ONLY = "MAINTENANCE-ONLY"
    NO_SEVERITY = "NO-SEVERITY"
