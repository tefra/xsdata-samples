from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


class TypeHotelPnrElement(Enum):
    """
    Defines the list of available data types for modifications.
    """
    GUARANTEE = "Guarantee"
    ASSOCIATED_REMARK = "AssociatedRemark"
    HOTEL_SPECIAL_REQUEST = "HotelSpecialRequest"
    CORPORATE_DISCOUNT_ID = "CorporateDiscountID"
    TRAVEL_PURPOSE = "TravelPurpose"
    LOYALTY_CARD = "LoyaltyCard"
    TRAVEL_COMPLIANCE = "TravelCompliance"
