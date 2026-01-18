from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowContentEnumSimple(Enum):
    """
    :cvar NO_SHOW_CONTENT: The content of the Xref.label is '''not'''
        rendered at the place of the reference.
    :cvar SHOW_CONTENT: The content of the element is rendered at the
        place of the reference.
    """

    NO_SHOW_CONTENT = "NO-SHOW-CONTENT"
    SHOW_CONTENT = "SHOW-CONTENT"
