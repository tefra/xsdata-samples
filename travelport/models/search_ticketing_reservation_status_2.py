from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


class SearchTicketingReservationStatus2(StrEnum):
    ON_HOLD = "OnHold"
    SET_FOR_TICKETING = "SetForTicketing"
    BOTH = "Both"
