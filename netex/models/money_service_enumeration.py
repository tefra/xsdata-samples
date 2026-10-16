from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MoneyServiceEnumeration(StrEnum):
    CASH_MACHINE = "cashMachine"
    BANK = "bank"
    INSURANCE = "insurance"
    BUREAU_DE_CHANGE = "bureauDeChange"
    CUSTOMS_OFFICE = "customsOffice"
