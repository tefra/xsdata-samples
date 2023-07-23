from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class GuaranteeInfoGuaranteeType(Enum):
    DEPOSIT = "Deposit"
    GUARANTEE = "Guarantee"
    PREPAYMENT = "Prepayment"
