from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SimpleVehicleCategoryEnumeration(Enum):
    SCOOTER = "scooter"
    CYCLE = "cycle"
    TRICYCLE = "tricycle"
    TANDEM = "tandem"
    MOPED = "moped"
    MOTORCYCLE = "motorcycle"
    QUADBIKE = "quadbike"
    CAR = "car"
    MICRO_CAR = "microCar"
    MINI_CAR = "miniCar"
    SMALL_CAR = "smallCar"
    MEDIUM_CAR = "mediumCar"
    LARGE_CAR = "largeCar"
    MINIVAN = "minivan"
    TRANSPORTER = "transporter"
    VAN = "van"
    SNOWMOBILE = "snowmobile"
