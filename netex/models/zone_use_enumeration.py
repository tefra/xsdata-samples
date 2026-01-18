from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ZoneUseEnumeration(Enum):
    FORBIDDEN_ZONE = "forbiddenZone"
    CANNOT_BOARD_AND_ALIGHT_IN_SAME_ZONE = "cannotBoardAndAlightInSameZone"
    CANNOT_BOARD_IN_ZONE = "cannotBoardInZone"
    CANNOT_ALIGHT_IN_ZONE = "cannotAlightInZone"
    MUST_BOARD_IN_ZONE = "mustBoardInZone"
    MUST_ALIGHT_IN_ZONE = "mustAlightInZone"
    PASS_THROUGH_USE_ONLY = "passThroughUseOnly"
    OTHER = "other"
