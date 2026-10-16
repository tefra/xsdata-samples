from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticMonitorUpdateKindEnumSimple(StrEnum):
    """
    :cvar ALWAYS: Dem shall accept every update.
    :cvar STEADY: Dem shall only accept if debouncing is at the limit.
    """

    ALWAYS = "ALWAYS"
    STEADY = "STEADY"
