from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DistributionRightsEnumeration(StrEnum):
    NONE = "none"
    SELL = "sell"
    EXCHANGE = "exchange"
    REFUND = "refund"
    INFORM = "inform"
    BOOK = "book"
    PRIVATE = "private"
    OTHER = "other"
