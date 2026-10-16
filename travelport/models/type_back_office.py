from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeBackOffice(StrEnum):
    ACCOUNTING = "Accounting"
    GLOBAL = "Global"
    NON_ACCOUNTING = "NonAccounting"
    NON_ACCOUNTING_REMOTE = "NonAccountingRemote"
    DUAL = "Dual"
