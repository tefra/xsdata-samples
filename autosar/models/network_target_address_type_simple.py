from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class NetworkTargetAddressTypeSimple(Enum):
    """
    :cvar FUNCTIONAL: Functional request type
    :cvar FUNCTIONAL_CAN_FD: Functional request type via CAN FD
    :cvar PHYSICAL: Physical request type
    :cvar PHYSICAL_CAN_FD: Physical request type via CAN FD
    """

    FUNCTIONAL = "FUNCTIONAL"
    FUNCTIONAL_CAN_FD = "FUNCTIONAL-CAN-FD"
    PHYSICAL = "PHYSICAL"
    PHYSICAL_CAN_FD = "PHYSICAL-CAN-FD"
