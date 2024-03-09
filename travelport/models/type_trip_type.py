from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeTripType(Enum):
    """
    Used in Low Fare Search to better target the results.
    """

    CHEAPEST = "Cheapest"
    QUICKEST = "Quickest"
    MOST_CONVENIENT = "MostConvenient"
    LEISURE = "Leisure"
    BUSINESS = "Business"
    LUXURY = "Luxury"
    PREFER_FIRST = "PreferFirst"
    BUSINESS_OR_FIRST = "BusinessOrFirst"
    NO_PENALTY = "NoPenalty"
