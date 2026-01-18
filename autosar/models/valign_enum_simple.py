from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ValignEnumSimple(Enum):
    """
    :cvar BOTTOM: The contents of the table cell is bottom aligned.
    :cvar MIDDLE: The contents of the table is vertically centered.
    :cvar TOP: The contents of the table cell is top aligned.
    """

    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"
    TOP = "TOP"
