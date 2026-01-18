from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameOperatorEnumeration(Enum):
    ANY = "any"
    SAME = "same"
    PARTICIPATING = "participating"
    DIFFERENT = "different"
