from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeVehicleChargeType(Enum):
    NO_CHARGE = "NoCharge"
    PERCENT = "Percent"
    RENTAL = "Rental"
    PER_CONTRACT = "PerContract"
    PER_HOUR = "PerHour"
    PER_DAY = "PerDay"
    PER_WEEK = "PerWeek"
    PER_MONTH = "PerMonth"
