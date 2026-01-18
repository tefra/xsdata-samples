from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PgwideEnumSimple(Enum):
    """
    :cvar NO_PGWIDE: This indicates that the table shall be fit in the
        current text flow.
    :cvar PGWIDE: This indicates that the table may use the entire page
        width. This is in particular important in case of so called
        "side-head layouts" but also if the table is in a list or in a
        note.
    """

    NO_PGWIDE = "NO-PGWIDE"
    PGWIDE = "PGWIDE"
