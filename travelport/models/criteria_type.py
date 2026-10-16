from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class CriteriaType(StrEnum):
    CORPORATE_DISCOUNT_ID = "CorporateDiscountID"
    PERMITTED_CHAINS = "PermittedChains"
    HOTEL_NAME = "HotelName"
    DISTANCE = "Distance"
    RATE_CATEGORY = "RateCategory"
    HOTEL_RATING = "HotelRating"
    AMENITIES = "Amenities"
    HOTEL_TRANSPORTATION = "HotelTransportation"
