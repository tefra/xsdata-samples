from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class DelayValueUnitType(Enum):
    """
    Indicates legal units for delay values.
    """

    PS = "ps"
    NS = "ns"
