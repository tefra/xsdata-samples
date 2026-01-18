from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoftwarePackageActivationActionEnumSimple(Enum):
    """
    :cvar REBOOT: Reboot the whole Machine.
    :cvar RESTART_APPLICATION: Restart the application software on the
        target Machine.
    :cvar WAIT_FOR_REBOOT: The installation has no immediate
        consequences in terms of other software on the target.
    """

    REBOOT = "REBOOT"
    RESTART_APPLICATION = "RESTART-APPLICATION"
    WAIT_FOR_REBOOT = "WAIT-FOR-REBOOT"
