from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MoneyFacilityEnumeration(Enum):
    OTHER = "other"
    CASH_MACHINE = "cashMachine"
    BANK = "bank"
    INSURANCE = "insurance"
    BUREAU_DE_CHANGE = "bureauDeChange"
