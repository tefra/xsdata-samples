from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class FaultSeverityCodeType(StrEnum):
    CRITICAL = "Critical"
    MAJOR = "Major"
    MINOR = "Minor"
    WARNING = "Warning"
    INFORMATION = "Information"
