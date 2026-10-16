from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


class SearchTicketingReservationStatus3(StrEnum):
    ON_HOLD = "OnHold"
    SET_FOR_TICKETING = "SetForTicketing"
    BOTH = "Both"
