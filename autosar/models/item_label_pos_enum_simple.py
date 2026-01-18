from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ItemLabelPosEnumSimple(Enum):
    """
    :cvar NEWLINE: The label is renders in a new line.
    :cvar NEWLINE_IF_NECESSARY: The label is rendered in a new line if
        it is longer than the indentation.
    :cvar NO_NEWLINE: The label is rendered in one line with the item
        even if it is longer than the indentation.
    """

    NEWLINE = "NEWLINE"
    NEWLINE_IF_NECESSARY = "NEWLINE-IF-NECESSARY"
    NO_NEWLINE = "NO-NEWLINE"
