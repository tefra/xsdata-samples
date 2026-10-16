from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class StairRampEnumeration(StrEnum):
    NONE = "none"
    BICYCLE = "bicycle"
    LUGGAGE = "luggage"
    STROLLER = "stroller"
    OTHER = "other"
    UNKNOWN = "unknown"
