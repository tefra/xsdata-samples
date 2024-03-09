from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class SearchTicketingReservationStatus5(Enum):
    ON_HOLD = "OnHold"
    SET_FOR_TICKETING = "SetForTicketing"
    BOTH = "Both"
