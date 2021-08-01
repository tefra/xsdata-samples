from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ParkingOccupancyEnum(Enum):
    """
    Parking Occupancy enum.

    :cvar EXPECT_CAR_PARK_TO_BE_FULL: Expect car park to be full.
    :cvar PERCENTAGE10: 10% full.
    :cvar PERCENTAGE20: 20% full.
    :cvar PERCENTAGE30: 30% full.
    :cvar PERCENTAGE40: 40% full.
    :cvar PERCENTAGE50: 50% full.
    :cvar PERCENTAGE60: 60% full.
    :cvar PERCENTAGE70: 70% full.
    :cvar PERCENTAGE80: 80% full.
    :cvar PERCENTAGE90: 90% full.
    :cvar FULL: Full.
    :cvar UNKNOWN: Unknown.
    """
    EXPECT_CAR_PARK_TO_BE_FULL = "expectCarParkToBeFull"
    PERCENTAGE10 = "percentage10"
    PERCENTAGE20 = "percentage20"
    PERCENTAGE30 = "percentage30"
    PERCENTAGE40 = "percentage40"
    PERCENTAGE50 = "percentage50"
    PERCENTAGE60 = "percentage60"
    PERCENTAGE70 = "percentage70"
    PERCENTAGE80 = "percentage80"
    PERCENTAGE90 = "percentage90"
    FULL = "full"
    UNKNOWN = "unknown"
