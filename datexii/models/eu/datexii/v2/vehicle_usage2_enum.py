from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VehicleUsage2Enum(Enum):
    """
    Vehicle usage types which are currently not supported in
    vehicleUsageType.

    :cvar CITY_LOGISTICS: Vehicles that are used to deliver goods in a
        city area.
    :cvar CAR_SHARING: Vehicles operated by a car-sharing company.
    """

    CITY_LOGISTICS = "cityLogistics"
    CAR_SHARING = "carSharing"
