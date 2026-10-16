from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class NvBlockNeedsWritingPriorityEnumSimple(StrEnum):
    """
    :cvar HIGH: Writing priority is high.
    :cvar LOW: Writing priority is low.
    :cvar MEDIUM: Writing priority is medium.
    """

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
