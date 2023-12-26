from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class DeductibleTypeDeductibleType(Enum):
    MAIN = "Main"
    PERIL_POLICY_DEDUCTIBLE = "PerilPolicyDeductible"
    PERIL_RISK_DEDUCTIBLE = "PerilRiskDeductible"
