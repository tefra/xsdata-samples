from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MarkingStatusEnumeration(Enum):
    NONE = "none"
    GOOD = "good"
    WORN = "worn"
    HAZARDOUS = "hazardous"
    UNKNOWN = "unknown"
