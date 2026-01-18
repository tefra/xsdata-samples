from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ChapterEnumBreakSimple(Enum):
    """
    :cvar BREAK: This indicates the a page break shall be applied before
        the current block.
    :cvar NO_BREAK: This indicates that there is no need to force a page
        break before this block.
    """

    BREAK = "BREAK"
    NO_BREAK = "NO-BREAK"
