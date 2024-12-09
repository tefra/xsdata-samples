from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class DelayValueType(Enum):
    """Indicates the type of delay value - minimum or maximum delay."""

    MIN = "min"
    MAX = "max"
