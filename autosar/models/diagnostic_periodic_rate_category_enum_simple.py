from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticPeriodicRateCategoryEnumSimple(Enum):
    """
    :cvar PERIODIC_RATE_FAST: This value represents a fast periodic
        rate.
    :cvar PERIODIC_RATE_MEDIUM: This value represents a medium periodic
        rate.
    :cvar PERIODIC_RATE_SLOW: This value represents a slow periodic
        rate.
    """

    PERIODIC_RATE_FAST = "PERIODIC-RATE-FAST"
    PERIODIC_RATE_MEDIUM = "PERIODIC-RATE-MEDIUM"
    PERIODIC_RATE_SLOW = "PERIODIC-RATE-SLOW"
