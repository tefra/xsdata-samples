from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DayEventEnumeration(StrEnum):
    ANY_DAY = "anyDay"
    NORMAL_DAY = "normalDay"
    MARKET_DAY = "marketDay"
    MATCH_DAY = "matchDay"
    EVENT_DAY = "eventDay"
