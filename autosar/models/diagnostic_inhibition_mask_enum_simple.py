from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticInhibitionMaskEnumSimple(Enum):
    """
    :cvar LAST_FAILED: This represents the inhibition mask behavior
        "last failed".
    :cvar NOT_TESTED: This represents the inhibition mask behavior "not
        tested".
    :cvar TESTED: This represents the inhibition mask behavior "tested".
    :cvar TESTED_AND_FAILED: This represents the inhibition mask
        behavior "tested and failed".
    """

    LAST_FAILED = "LAST-FAILED"
    NOT_TESTED = "NOT-TESTED"
    TESTED = "TESTED"
    TESTED_AND_FAILED = "TESTED-AND-FAILED"
