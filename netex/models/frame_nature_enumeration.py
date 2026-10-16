from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FrameNatureEnumeration(StrEnum):
    PLANNED = "planned"
    OPERATIONAL = "operational"
    CONTINGENCY_PLAN = "contingencyPlan"
    OTHER = "other"
