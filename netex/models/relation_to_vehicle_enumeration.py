from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RelationToVehicleEnumeration(StrEnum):
    FRONT_LEFT = "frontLeft"
    FRONT_RIGHT = "frontRight"
    BACK_RIGHT = "backRight"
    DRIVER_LEFT = "driverLeft"
    DRIVER_RIGHT = "driverRight"
