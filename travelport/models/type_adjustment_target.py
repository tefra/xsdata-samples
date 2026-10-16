from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeAdjustmentTarget(StrEnum):
    BASE = "Base"
    TOTAL = "Total"
    OTHER = "Other"
