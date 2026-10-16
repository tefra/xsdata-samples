from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeDepositGuaranteeType(StrEnum):
    NUMBER_OF_DAYS = "NumberOfDays"
    AMOUNT = "Amount"
    PERCENT = "Percent"
