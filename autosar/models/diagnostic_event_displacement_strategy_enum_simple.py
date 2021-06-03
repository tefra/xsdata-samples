from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticEventDisplacementStrategyEnumSimple(Enum):
    """
    :cvar FULL: Event memory entry displacement is enabled, by
        consideration of priority active/passive status, and occurrence.
    :cvar NONE_VALUE: Event memory entry displacement is disabled.
    :cvar PRIO_OCC: Event memory entry displacement is enabled, by
        consideration of priority and occurrence (but without
        active/passive status).
    """
    FULL = "FULL"
    NONE_VALUE = "NONE"
    PRIO_OCC = "PRIO-OCC"
