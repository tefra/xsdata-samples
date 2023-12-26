from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypePurchaseWindow(Enum):
    """
    The purchase windows available for merchandising service.
    """

    BOOKING_ONLY = "BookingOnly"
    TICKETING_ONLY = "TicketingOnly"
    CHECK_IN_ONLY = "CheckInOnly"
    ANYTIME = "Anytime"
    POST_TICKETING = "PostTicketing"
