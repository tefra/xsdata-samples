from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntitlementTypeEnumeration(StrEnum):
    NONE = "none"
    PURCHASE = "purchase"
    PURCHASE_AT_DISCOUNT = "purchaseAtDiscount"
    USE = "use"
    OTHER = "other"
