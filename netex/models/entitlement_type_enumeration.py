from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntitlementTypeEnumeration(Enum):
    NONE = "none"
    PURCHASE = "purchase"
    PURCHASE_AT_DISCOUNT = "purchaseAtDiscount"
    USE = "use"
    OTHER = "other"
