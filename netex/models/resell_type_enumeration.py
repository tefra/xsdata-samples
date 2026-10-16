from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ResellTypeEnumeration(StrEnum):
    NONE = "none"
    PARTIAL = "partial"
    SLIDING_SCALE = "slidingScale"
    FULL = "full"
