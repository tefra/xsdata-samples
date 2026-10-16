from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CrowdingEnumeration(StrEnum):
    VERY_QUIET = "veryQuiet"
    QUIET = "quiet"
    NORMAL = "normal"
    BUSY = "busy"
    VERY_BUSY = "veryBusy"
