from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


class TypeCommissionType6(Enum):
    """
    Types of possible commission.
    """
    FLAT = "Flat"
    PERCENT_BASE = "PercentBase"
    PERCENT_TOTAL = "PercentTotal"
