from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ShowSeeEnumSimple(Enum):
    """
    :cvar NO_SHOW_SEE: The word "see" is '''not''' rendered before  the
        reference.
    :cvar SHOW_SEE: The word "see"is rendered before the reference.
    """

    NO_SHOW_SEE = "NO-SHOW-SEE"
    SHOW_SEE = "SHOW-SEE"
