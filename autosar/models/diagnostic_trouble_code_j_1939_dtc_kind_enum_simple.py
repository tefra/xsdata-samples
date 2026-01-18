from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticTroubleCodeJ1939DtcKindEnumSimple(Enum):
    """
    :cvar SERVICE_ONLY: this represents a DTC that is only relevant for
        service in a garage, reported by e.g. DM53.
    :cvar STANDARD: This represents a non-specific DTC reported by e.g.
        DM1.
    """

    SERVICE_ONLY = "SERVICE-ONLY"
    STANDARD = "STANDARD"
