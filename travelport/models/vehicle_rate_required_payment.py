from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class VehicleRateRequiredPayment(Enum):
    GUARANTEE = "Guarantee"
    DEPOSIT = "Deposit"
    PRE_PAYMENT = "PrePayment"
