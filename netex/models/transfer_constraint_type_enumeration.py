from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TransferConstraintTypeEnumeration(StrEnum):
    CAN_TRANSFER = "canTransfer"
    CANNOT_TRANSFER = "cannotTransfer"
    OTHER = "other"
