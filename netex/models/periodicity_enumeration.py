from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PeriodicityEnumeration(Enum):
    ANNUAL = "annual"
    QUARTERLY = "quarterly"
    MONTHLY = "monthly"
    WEEKLY = "weekly"
    DAILY = "daily"
