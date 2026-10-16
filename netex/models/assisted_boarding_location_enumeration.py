from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AssistedBoardingLocationEnumeration(StrEnum):
    BOARD_AT_ANY_DOOR = "boardAtAnyDoor"
    BOARD_ONLY_AT_SPECIFIED_POSITIONS = "boardOnlyAtSpecifiedPositions"
    UNKNOWN = "unknown"
