from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class IsFlowControlFlowType(StrEnum):
    CREDIT_RETURN = "credit-return"
    READY = "ready"
    BUSY = "busy"
    USER = "user"
