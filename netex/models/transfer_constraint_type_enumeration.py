from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransferConstraintTypeEnumeration(Enum):
    CAN_TRANSFER = "canTransfer"
    CANNOT_TRANSFER = "cannotTransfer"
    OTHER = "other"
