from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TideEnumeration(StrEnum):
    HIGH_TIDE = "HighTide"
    LOW_TIDE = "LowTide"
    NEAP_TIDE = "NeapTide"
    ALL_TIDES = "AllTides"
