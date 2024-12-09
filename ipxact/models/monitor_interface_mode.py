from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class MonitorInterfaceMode(Enum):
    INITIATOR = "initiator"
    TARGET = "target"
    SYSTEM = "system"
    MIRRORED_INITIATOR = "mirroredInitiator"
    MIRRORED_TARGET = "mirroredTarget"
    MIRRORED_SYSTEM = "mirroredSystem"
