from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LightingEnumeration(StrEnum):
    WELL_LIT = "wellLit"
    POORLY_LIT = "poorlyLit"
    UNLIT = "unlit"
    UNKNOWN = "unknown"
    OTHER = "other"
