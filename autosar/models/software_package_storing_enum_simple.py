from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoftwarePackageStoringEnumSimple(Enum):
    """
    :cvar NONE: No storing in vehicle.
    :cvar UCM: Storing in UCM (subordinate).
    :cvar UCM_MASTER: Storing in Ucm Master.
    """

    NONE = "NONE"
    UCM = "UCM"
    UCM_MASTER = "UCM-MASTER"
