from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowResourceTypeEnumSimple(StrEnum):
    """
    :cvar NO_SHOW_TYPE: The type of the target is '''not''' rendered at
        the place of the reference.
    :cvar SHOW_TYPE: The type of the target is rendered at the place of
        the reference.
    """

    NO_SHOW_TYPE = "NO-SHOW-TYPE"
    SHOW_TYPE = "SHOW-TYPE"
