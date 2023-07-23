from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class TypeCommissionLevel5(Enum):
    """
    ATA/IATA Standard commission level.
    """
    RECALLED = "Recalled"
    FARE = "Fare"
    PENALTY = "Penalty"
