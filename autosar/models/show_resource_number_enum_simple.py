from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowResourceNumberEnumSimple(Enum):
    """
    :cvar NO_SHOW_NUMBER: The number of the target is '''not''' rendered
        at the place of the reference.
    :cvar SHOW_NUMBER: The number of the target is rendered at the place
        of the reference.
    """

    NO_SHOW_NUMBER = "NO-SHOW-NUMBER"
    SHOW_NUMBER = "SHOW-NUMBER"
