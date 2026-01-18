from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class NmCoordinatorRoleEnumSimple(Enum):
    """
    :cvar ACTIVE: Coordinator which "actively" performs NmCoordinator
        functionality at this channel
    :cvar PASSIVE: Coordinator which "passively" performs NmCoordinator
        functionality at this channel - used at NmCoordinatorSync use
        case.
    """

    ACTIVE = "ACTIVE"
    PASSIVE = "PASSIVE"
