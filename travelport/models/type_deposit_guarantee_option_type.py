from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeDepositGuaranteeOptionType(Enum):
    AFTER_BOOKING = "AfterBooking"
    PRIOR_TO_PICKUP = "PriorToPickup"
