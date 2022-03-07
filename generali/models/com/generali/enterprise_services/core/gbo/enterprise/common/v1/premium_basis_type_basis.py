from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"


class PremiumBasisTypeBasis(Enum):
    ESTIMATED_VALUE = "EstimatedValue"
    VALUE = "Value"
    PERCENTAGE = "Percentage"
