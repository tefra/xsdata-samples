from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class ComponentPortDirectionType(Enum):
    """
    The direction of a component port.
    """

    IN = "in"
    OUT = "out"
    INOUT = "inout"
    PHANTOM = "phantom"
