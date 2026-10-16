from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeDisplayCategory(StrEnum):
    """
    Type of booking.
    """

    WITH_ITINERARY_PRICING = "With Itinerary Pricing"
    STORE = "Store"
    SPECIAL_SERVICE = "SpecialService"
