from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class DeductibleTypeDeductibleType(StrEnum):
    MAIN = "Main"
    PERIL_POLICY_DEDUCTIBLE = "PerilPolicyDeductible"
    PERIL_RISK_DEDUCTIBLE = "PerilRiskDeductible"
