from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GatedEnumeration(StrEnum):
    GATED_AREA = "gatedArea"
    OPEN_AREA = "openArea"
    UNKNOWN = "unknown"
