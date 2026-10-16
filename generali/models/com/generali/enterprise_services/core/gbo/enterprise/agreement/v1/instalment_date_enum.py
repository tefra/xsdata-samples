from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class InstalmentDateEnum(StrEnum):
    ACCOUNTING_DATE = "AccountingDate"
    DUE_DATE = "DueDate"
