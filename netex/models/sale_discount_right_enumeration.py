from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SaleDiscountRightEnumeration(StrEnum):
    TRAVEL_CARD = "travelCard"
    PAY_AS_YOU_GO_RIGHT = "payAsYouGoRight"
    STATUTORY_RIGHT = "statutoryRight"
    OTHER = "other"
