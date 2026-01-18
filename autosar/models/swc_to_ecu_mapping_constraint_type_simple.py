from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SwcToEcuMappingConstraintTypeSimple(Enum):
    """
    :cvar DEDICATED: Dedicated mapping means that the SW-C can only be
        mapped to the ECUs it is dedicated to.
    :cvar EXCLUSIVE: Exclusive mapping means that the SW-C cannot be
        mapped to the ECUs it is excluded from.
    """

    DEDICATED = "DEDICATED"
    EXCLUSIVE = "EXCLUSIVE"
