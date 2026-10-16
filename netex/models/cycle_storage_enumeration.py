from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CycleStorageEnumeration(StrEnum):
    RACKS = "racks"
    DOCKS = "docks"
    BARS = "bars"
    RAILINGS = "railings"
    CYCLE_SCHEME = "cycleScheme"
    LOCKERS = "lockers"
    FREESTANDING = "freestanding"
    OTHER = "other"
