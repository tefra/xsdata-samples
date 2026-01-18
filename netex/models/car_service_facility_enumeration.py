from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CarServiceFacilityEnumeration(Enum):
    UNKNOWN = "unknown"
    VALET_PARKING = "valetParking"
    CAR_WASH = "carWash"
    VALET_CAR_WASH = "valetCarWash"
    CAR_VALET_CLEAN = "carValetClean"
    OIL_CHANGE = "oilChange"
    ENGINE_WARMING = "engineWarming"
    PETROL = "petrol"
    BATTERY_CARE = "batteryCare"
    RECHARGING = "recharging"
    TYRE_CHECK = "tyreCheck"
    OTHER = "other"
