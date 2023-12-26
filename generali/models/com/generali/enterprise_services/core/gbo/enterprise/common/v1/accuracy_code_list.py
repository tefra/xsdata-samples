from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


class AccuracyCodeList(Enum):
    ACTUAL = "Actual"
    ESTIMATED = "Estimated"
    MODELED = "Modeled"
    NOT_AVAILABLE = "NotAvailable"
