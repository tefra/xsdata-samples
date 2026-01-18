from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingSpacePhysicsEnum(Enum):
    """
    Specifies drive through and open air properties for the parking space
    or the group of parking spaces.

    :cvar DRIVE_THROUGH: Entering as well as leaving the parking space
        can be done straight in the direction of parking.
    :cvar OPEN_AIR: There is no roof and not another storey on top of
        the parking space, which could prevent from rain, for example.
    """

    DRIVE_THROUGH = "driveThrough"
    OPEN_AIR = "openAir"
