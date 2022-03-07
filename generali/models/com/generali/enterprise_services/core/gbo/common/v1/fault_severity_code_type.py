from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class FaultSeverityCodeType(Enum):
    CRITICAL = "Critical"
    MAJOR = "Major"
    MINOR = "Minor"
    WARNING = "Warning"
    INFORMATION = "Information"
