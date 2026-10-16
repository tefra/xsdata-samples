from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameTypeOfProductCategoryEnumeration(StrEnum):
    ANY = "any"
    SAME = "same"
    SAME_OR_EQUIVALENT = "sameOrEquivalent"
    DIFFERENT = "different"
