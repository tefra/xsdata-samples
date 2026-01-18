from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CouchetteFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    T2 = "T2"
    T3 = "T3"
    C1 = "C1"
    C2 = "C2"
    C4 = "C4"
    C5 = "C5"
    C6 = "C6"
    WHEELCHAIR = "wheelchair"
    OTHER = "other"
