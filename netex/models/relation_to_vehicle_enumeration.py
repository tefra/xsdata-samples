from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RelationToVehicleEnumeration(Enum):
    FRONT_LEFT = "frontLeft"
    FRONT_RIGHT = "frontRight"
    BACK_RIGHT = "backRight"
    DRIVER_LEFT = "driverLeft"
    DRIVER_RIGHT = "driverRight"
