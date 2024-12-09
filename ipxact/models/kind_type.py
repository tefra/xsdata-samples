from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class KindType(Enum):
    TLM_PORT = "tlm_port"
    TLM_SOCKET = "tlm_socket"
    SIMPLE_SOCKET = "simple_socket"
    MULTI_SOCKET = "multi_socket"
    CUSTOM = "custom"
