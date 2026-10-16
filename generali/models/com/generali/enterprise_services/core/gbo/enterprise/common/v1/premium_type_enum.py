from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


class PremiumTypeEnum(StrEnum):
    GROSS = "Gross"
    NET = "Net"
