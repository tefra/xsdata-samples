from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeDepositGuaranteeOptionType(StrEnum):
    AFTER_BOOKING = "AfterBooking"
    PRIOR_TO_PICKUP = "PriorToPickup"
