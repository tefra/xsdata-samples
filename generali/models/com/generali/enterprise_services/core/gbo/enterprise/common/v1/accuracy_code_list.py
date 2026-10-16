from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/common/v1"
)


class AccuracyCodeList(StrEnum):
    ACTUAL = "Actual"
    ESTIMATED = "Estimated"
    MODELED = "Modeled"
    NOT_AVAILABLE = "NotAvailable"
