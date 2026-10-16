from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingChargeTypeEnumeration(StrEnum):
    FULL_AMOUNT = "fullAmount"
    BLOCK_FULL_AMOUNT_ON_CARD = "blockFullAmountOnCard"
    DEPOSIT = "deposit"
    NONE = "none"
    OTHER = "other"
