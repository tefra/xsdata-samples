from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingVisibilityEnumeration(Enum):
    UNMARKED = "unmarked"
    SIGNAGE_ONLY = "signageOnly"
    DEMARCATED = "demarcated"
    DOCKS = "docks"
    OTHER = "other"
