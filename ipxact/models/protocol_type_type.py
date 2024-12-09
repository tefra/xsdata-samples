from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class ProtocolTypeType(Enum):
    TLM = "tlm"
    CUSTOM = "custom"
