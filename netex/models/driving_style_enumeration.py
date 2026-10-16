from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DrivingStyleEnumeration(StrEnum):
    SEDATE = "sedate"
    MODERATE = "moderate"
    FAST = "fast"
    OTHER = "other"
