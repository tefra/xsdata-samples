from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFarePenaltyPenaltyApplies(StrEnum):
    """
    The values can be "Anytime", "Before Departure" or "After Departure".
    """

    ANYTIME = "Anytime"
    BEFORE_DEPARTURE = "Before Departure"
    AFTER_DEPARTURE = "After Departure"
