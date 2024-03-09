from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


class TypeAirPnrElement(Enum):
    """
    Defines the list of available data types for modifications.
    """

    PAYMENT = "Payment"
    ASSOCIATED_REMARK = "AssociatedRemark"
    TICKETING_MODIFIERS = "TicketingModifiers"
    CREDIT_CARD_AUTHORIZATION = "CreditCardAuthorization"
    SSR = "SSR"
    LOYALTY_CARD = "LoyaltyCard"
    TRAVEL_COMPLIANCE = "TravelCompliance"
