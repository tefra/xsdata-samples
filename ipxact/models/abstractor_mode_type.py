from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class AbstractorModeType(Enum):
    """
    Mode for this abstractor.
    """

    INITIATOR = "initiator"
    TARGET = "target"
    DIRECT = "direct"
    SYSTEM = "system"
