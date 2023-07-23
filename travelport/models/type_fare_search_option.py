from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareSearchOption(Enum):
    """
    Fare Search option indicator.
    """
    LEAVE = "Leave"
    RETURN = "Return"
    SEASONAL = "Seasonal"
    BLACKOUT = "Blackout"
    ADVANCE_PURCHASE = "Advance Purchase"
    DAY_OF_WEEK = "Day-of-week"
    EFFECTIVE_DATE = "Effective Date"
