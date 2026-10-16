from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class SictypeEnum(StrEnum):
    DIVISION = "Division"
    MAJOR_GROUP = "MajorGroup"
    INDUSTRY_GROUP = "IndustryGroup"
    INDUSTRY = "Industry"
    SUB_INDUSTRY = "Sub-Industry"
