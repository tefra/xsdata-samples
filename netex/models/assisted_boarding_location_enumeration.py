from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistedBoardingLocationEnumeration(Enum):
    BOARD_AT_ANY_DOOR = "boardAtAnyDoor"
    BOARD_ONLY_AT_SPECIFIED_POSITIONS = "boardOnlyAtSpecifiedPositions"
    UNKNOWN = "unknown"
