from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypePricingType(Enum):
    CLASS_BOOKED = "ClassBooked"
    LOWEST_CLASS = "LowestClass"
    LOWEST_QUOTE = "LowestQuote"
