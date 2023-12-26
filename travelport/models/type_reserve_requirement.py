from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeReserveRequirement(Enum):
    """
    Type of payment required to reserve travel i.e. Hotel Reservation requirement.
    """

    DEPOSIT = "Deposit"
    GUARANTEE = "Guarantee"
    PREPAYMENT = "Prepayment"
    OTHER = "Other"
