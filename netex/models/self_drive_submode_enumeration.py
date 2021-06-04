from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SelfDriveSubmodeEnumeration(Enum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    HIRE_CAR = "hireCar"
    HIRE_VAN = "hireVan"
    HIRE_MOTORBIKE = "hireMotorbike"
    HIRE_CYCLE = "hireCycle"
    ALL_HIRE_VEHICLES = "allHireVehicles"
