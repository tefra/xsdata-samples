from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class LegalCostTypeCostType(Enum):
    INCLUSIVE = "Inclusive"
    UNLIMITED = "Unlimited"
    FIX_AMOUNT = "FixAmount"
    PERCENT_OF_LIMIT = "PercentOfLimit"
