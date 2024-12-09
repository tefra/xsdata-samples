from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class Direction(Enum):
    IN = "in"
    OUT = "out"
    INOUT = "inout"
