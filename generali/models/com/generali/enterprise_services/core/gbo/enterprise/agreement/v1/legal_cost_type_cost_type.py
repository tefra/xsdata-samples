from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class LegalCostTypeCostType(StrEnum):
    INCLUSIVE = "Inclusive"
    UNLIMITED = "Unlimited"
    FIX_AMOUNT = "FixAmount"
    PERCENT_OF_LIMIT = "PercentOfLimit"
