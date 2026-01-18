from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticTestResultUpdateEnumSimple(Enum):
    """
    :cvar ALWAYS: Any DTR result reported by the monitor is used by the
        Dem.
    :cvar STEADY: The Dem accepts reported DTRs only when the configured
        debouncing mechanism is stable at the FAIL or PASS limit.
    """

    ALWAYS = "ALWAYS"
    STEADY = "STEADY"
