from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeAdjustmentTarget(Enum):
    BASE = "Base"
    TOTAL = "Total"
    OTHER = "Other"
