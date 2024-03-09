from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeBackOffice(Enum):
    ACCOUNTING = "Accounting"
    GLOBAL = "Global"
    NON_ACCOUNTING = "NonAccounting"
    NON_ACCOUNTING_REMOTE = "NonAccountingRemote"
    DUAL = "Dual"
