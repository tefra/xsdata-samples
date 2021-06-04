from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CustomerPurchasePackageStatusEnumeration(Enum):
    RESERVED = "reserved"
    ORDERED = "ordered"
    PAID_FOR = "paidFor"
    UNUSED = "unused"
    ACTIVATED = "activated"
    PARTIALLY_USED = "partiallyUsed"
    USED = "used"
    ARCHIVED = "archived"
    OTHER = "other"
