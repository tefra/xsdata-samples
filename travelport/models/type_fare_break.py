from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareBreak(Enum):
    """
    Types of fare break.

    Properties
    ----------
    MUST_BREAK
        Break Fare at the associated segment. Multiple Breaks or No Breaks
        may be allowed.
    MUST_ONLY_BREAK
        Only Break Fare at the associated segment. Fare Break in the entire
        itinerary is allowed only at the concerned segment.
    MUST_NOT_BREAK
        No Fare Break allowed at the associated segment.
    """
    MUST_BREAK = "MustBreak"
    MUST_ONLY_BREAK = "MustOnlyBreak"
    MUST_NOT_BREAK = "MustNotBreak"
