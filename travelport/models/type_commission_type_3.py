from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


class TypeCommissionType3(StrEnum):
    """
    Types of possible commission.
    """

    FLAT = "Flat"
    PERCENT_BASE = "PercentBase"
    PERCENT_TOTAL = "PercentTotal"
