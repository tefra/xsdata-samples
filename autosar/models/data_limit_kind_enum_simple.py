from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataLimitKindEnumSimple(StrEnum):
    """
    :cvar MAX: Limitation to maximum value
    :cvar MIN: Limitation to minimum value
    :cvar NONE: No limitation applicable
    """

    MAX = "MAX"
    MIN = "MIN"
    NONE = "NONE"
