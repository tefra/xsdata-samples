from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IntervalTypeEnumSimple(Enum):
    """
    :cvar CLOSED: The area is limited by the value given. The value
        itself is included.
    :cvar INFINITE: This indicates that the limit is infinite. Note, it
        is obsolete. Use INF / -INF as value of the limit.
    :cvar OPEN: The area is limited by the value given. The value itself
        is not included.
    """

    CLOSED = "CLOSED"
    INFINITE = "INFINITE"
    OPEN = "OPEN"
