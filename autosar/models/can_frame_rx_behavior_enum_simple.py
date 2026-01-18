from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CanFrameRxBehaviorEnumSimple(Enum):
    """
    :cvar ANY: This CAN frame may be received as both, CAN 2.0 and CAN
        FD.
    :cvar CAN_20: This CAN frame shall be received as CAN 2.0 only. In
        case the CAN frame is received as CAN FD it is discarded during
        reception.
    :cvar CAN_FD: This CAN frame shall be received as CAN FD only. In
        case the CAN frame is received as CAN 2.0 it is discarded during
        reception.
    """

    ANY = "ANY"
    CAN_20 = "CAN-20"
    CAN_FD = "CAN-FD"
