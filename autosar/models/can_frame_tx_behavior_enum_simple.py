from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CanFrameTxBehaviorEnumSimple(Enum):
    """
    :cvar CAN_20: This CAN frame shall be sent as CAN 2.0 only.
    :cvar CAN_FD: This CAN frame shall be sent as CAN FD.
    """

    CAN_20 = "CAN-20"
    CAN_FD = "CAN-FD"
