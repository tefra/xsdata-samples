from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LineTypeEnumeration(StrEnum):
    LOCAL = "local"
    URBAN = "urban"
    LONG_DISTANCE = "longDistance"
    EXPRESS = "express"
    SEASONAL = "seasonal"
    REPLACEMENT = "replacement"
    FLEXIBLE = "flexible"
    OTHER = "other"
