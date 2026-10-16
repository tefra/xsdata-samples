from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DiscountBasisEnumeration(StrEnum):
    NONE = "none"
    FREE = "free"
    DISCOUNT = "discount"
