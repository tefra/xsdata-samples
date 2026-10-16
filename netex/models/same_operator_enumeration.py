from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameOperatorEnumeration(StrEnum):
    ANY = "any"
    SAME = "same"
    PARTICIPATING = "participating"
    DIFFERENT = "different"
