from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class CellClassValueType(Enum):
    """
    Indicates legal cell class values.
    """

    COMBINATIONAL = "combinational"
    SEQUENTIAL = "sequential"
