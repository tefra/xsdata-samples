from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class CoverTypeEnum(StrEnum):
    FLEXA = "Flexa"
    ALL_RISKS = "AllRisks"
    TERRORISM = "Terrorism"
