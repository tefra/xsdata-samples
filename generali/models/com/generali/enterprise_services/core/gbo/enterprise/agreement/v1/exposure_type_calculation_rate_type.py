from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class ExposureTypeCalculationRateType(Enum):
    AVERAGE_VALUE = "AverageValue"
    PERCENTAGE = "Percentage"
    ACTUAL_VALUE = "ActualValue"
