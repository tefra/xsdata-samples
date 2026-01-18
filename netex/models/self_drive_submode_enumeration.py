from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SelfDriveSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    HIRE_SCOOTER = "hireScooter"
    HIRE_CYCLE = "hireCycle"
    HIRE_MOTORBIKE = "hireMotorbike"
    HIRE_CAR = "hireCar"
    HIRE_VAN = "hireVan"
    OWN_SCOOTER = "ownScooter"
    OWN_CYCLE = "ownCycle"
    OWN_MOTORBIKE = "ownMotorbike"
    OWN_CAR = "ownCar"
    OWN_VAN = "ownVan"
    ALL_HIRE_VEHICLES = "allHireVehicles"
    ALL_VEHICLES = "allVehicles"
