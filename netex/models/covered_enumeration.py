from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CoveredEnumeration(StrEnum):
    INDOORS = "indoors"
    OUTDOORS = "outdoors"
    COVERED = "covered"
    MIXED = "mixed"
    UNKNOWN = "unknown"
