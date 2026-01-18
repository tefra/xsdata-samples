from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DistributionRightsEnumeration(Enum):
    NONE = "none"
    SELL = "sell"
    EXCHANGE = "exchange"
    REFUND = "refund"
    INFORM = "inform"
    BOOK = "book"
    PRIVATE = "private"
    OTHER = "other"
