from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CoveredEnumeration(Enum):
    INDOORS = "indoors"
    OUTDOORS = "outdoors"
    COVERED = "covered"
    MIXED = "mixed"
    UNKNOWN = "unknown"
