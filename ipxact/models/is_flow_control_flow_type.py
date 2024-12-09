from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class IsFlowControlFlowType(Enum):
    CREDIT_RETURN = "credit-return"
    READY = "ready"
    BUSY = "busy"
    USER = "user"
