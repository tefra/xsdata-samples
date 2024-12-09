from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class CellStrengthValueType(Enum):
    """
    Indicates legal cell strength values.
    """

    LOW = "low"
    MEDIAN = "median"
    HIGH = "high"
