from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingVisibilityEnumeration(StrEnum):
    UNMARKED = "unmarked"
    SIGNAGE_ONLY = "signageOnly"
    DEMARCATED = "demarcated"
    DOCKS = "docks"
    OTHER = "other"
