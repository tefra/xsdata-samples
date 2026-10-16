from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class TypeCommissionType4(StrEnum):
    """
    Types of possible commission.
    """

    FLAT = "Flat"
    PERCENT_BASE = "PercentBase"
    PERCENT_TOTAL = "PercentTotal"
