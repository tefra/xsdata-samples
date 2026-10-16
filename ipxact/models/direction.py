from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class Direction(StrEnum):
    IN = "in"
    OUT = "out"
    INOUT = "inout"
