from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class ExposureTypeApplyRateType(StrEnum):
    RATE = "Rate"
    FLAT = "Flat"
    PER_MILLS = "PerMills"
    UNIT = "Unit"
