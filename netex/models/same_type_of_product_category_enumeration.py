from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameTypeOfProductCategoryEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    SAME_OR_EQUIVALENT = "sameOrEquivalent"
    DIFFERENT = "different"
