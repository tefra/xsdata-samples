from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameJourneyEnumeration(StrEnum):
    ANY = "any"
    SAME = "same"
    SIMILAR = "similar"
    DIFFERENT = "different"
