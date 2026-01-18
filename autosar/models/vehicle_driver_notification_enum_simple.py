from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class VehicleDriverNotificationEnumSimple(Enum):
    """
    :cvar ACTIVATE: Software package shall be activated.
    :cvar FINISH: Finish notification
    :cvar PROCESS: Processing of software package shall be executed
    :cvar ROLL_BACK: Software package shall be rolled back.
    :cvar TRANSFER: Software shall be transferred to the vehicle.
    """

    ACTIVATE = "ACTIVATE"
    FINISH = "FINISH"
    PROCESS = "PROCESS"
    ROLL_BACK = "ROLL-BACK"
    TRANSFER = "TRANSFER"
