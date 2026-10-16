from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ZoneTopologyEnumeration(StrEnum):
    OVERLAPPING = "overlapping"
    HONEYCOMB = "honeycomb"
    RING = "ring"
    ANNULAR = "annular"
    NESTED = "nested"
    TILED = "tiled"
    SEQUENCE = "sequence"
    OVERLAPPING_SEQUENCE = "overlappingSequence"
    OTHER = "other"
