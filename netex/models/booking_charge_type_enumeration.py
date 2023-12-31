from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingChargeTypeEnumeration(Enum):
    FULL_AMOUNT = "fullAmount"
    BLOCK_FULL_AMOUNT_ON_CARD = "blockFullAmountOnCard"
    DEPOSIT = "deposit"
    NONE = "none"
    OTHER = "other"
