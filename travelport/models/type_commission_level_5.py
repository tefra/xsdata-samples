from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class TypeCommissionLevel5(StrEnum):
    """
    ATA/IATA Standard commission level.
    """

    RECALLED = "Recalled"
    FARE = "Fare"
    PENALTY = "Penalty"
