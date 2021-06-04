from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AllVehicleModesOfTransportEnumeration(Enum):
    ALL = "all"
    UNKNOWN = "unknown"
    BUS = "bus"
    TROLLEY_BUS = "trolleyBus"
    TRAM = "tram"
    COACH = "coach"
    RAIL = "rail"
    INTERCITY_RAIL = "intercityRail"
    URBAN_RAIL = "urbanRail"
    METRO = "metro"
    AIR = "air"
    WATER = "water"
    CABLEWAY = "cableway"
    FUNICULAR = "funicular"
    SNOW_AND_ICE = "snowAndIce"
    TAXI = "taxi"
    SELF_DRIVE = "selfDrive"
