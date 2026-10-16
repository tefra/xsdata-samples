from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class TypeCommissionLevel4(StrEnum):
    """
    ATA/IATA Standard commission level.
    """

    RECALLED = "Recalled"
    FARE = "Fare"
    PENALTY = "Penalty"
