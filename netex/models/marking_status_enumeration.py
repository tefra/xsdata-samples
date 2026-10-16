from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MarkingStatusEnumeration(StrEnum):
    NONE = "none"
    GOOD = "good"
    WORN = "worn"
    HAZARDOUS = "hazardous"
    UNKNOWN = "unknown"
