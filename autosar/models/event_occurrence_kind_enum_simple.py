from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EventOccurrenceKindEnumSimple(StrEnum):
    """
    :cvar MULTIPLE_OCCURRENCES: Specifies that an event may occur more
        than once in a given time interval.
    :cvar SINGLE_OCCURRENCE: Specifies that an event shall occur only
        once in a given time interval.
    """

    MULTIPLE_OCCURRENCES = "MULTIPLE-OCCURRENCES"
    SINGLE_OCCURRENCE = "SINGLE-OCCURRENCE"
