from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeCommissionLevel1(Enum):
    """
    ATA/IATA Standard commission level.
    """

    RECALLED = "Recalled"
    FARE = "Fare"
    PENALTY = "Penalty"
