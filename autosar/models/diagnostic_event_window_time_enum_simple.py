from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticEventWindowTimeEnumSimple(Enum):
    """
    :cvar EVENT_WINDOW_CURRENT_AND_FOLLOWING_CYCLE: This means that the
        window extends to this and the following cycle.
    :cvar EVENT_WINDOW_CURRENT_CYCLE: This means that the window is
        limited to the current cycle.
    :cvar EVENT_WINDOW_INFINITE: This means that the window extents
        without a border.
    """

    EVENT_WINDOW_CURRENT_AND_FOLLOWING_CYCLE = (
        "EVENT-WINDOW-CURRENT-AND-FOLLOWING-CYCLE"
    )
    EVENT_WINDOW_CURRENT_CYCLE = "EVENT-WINDOW-CURRENT-CYCLE"
    EVENT_WINDOW_INFINITE = "EVENT-WINDOW-INFINITE"
