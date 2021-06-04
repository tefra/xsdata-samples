from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DayEventEnumeration(Enum):
    ANY_DAY = "anyDay"
    NORMAL_DAY = "normalDay"
    MARKET_DAY = "marketDay"
    MATCH_DAY = "matchDay"
    EVENT_DAY = "eventDay"
