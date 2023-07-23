from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class CriteriaType(Enum):
    CORPORATE_DISCOUNT_ID = "CorporateDiscountID"
    PERMITTED_CHAINS = "PermittedChains"
    HOTEL_NAME = "HotelName"
    DISTANCE = "Distance"
    RATE_CATEGORY = "RateCategory"
    HOTEL_RATING = "HotelRating"
    AMENITIES = "Amenities"
    HOTEL_TRANSPORTATION = "HotelTransportation"
