from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/enterprise/agreement/v1"
)


class InstalmentDateEnum(Enum):
    ACCOUNTING_DATE = "AccountingDate"
    DUE_DATE = "DueDate"
