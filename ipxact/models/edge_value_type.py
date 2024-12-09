from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class EdgeValueType(Enum):
    """
    Indicates legal values for edge specification attributes.
    """

    RISE = "rise"
    FALL = "fall"
