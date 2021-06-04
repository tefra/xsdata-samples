from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AllModesEnumeration(Enum):
    ALL = "all"
    UNKNOWN = "unknown"
    AIR = "air"
    BUS = "bus"
    TROLLEY_BUS = "trolleyBus"
    TRAM = "tram"
    COACH = "coach"
    RAIL = "rail"
    INTERCITY_RAIL = "intercityRail"
    URBAN_RAIL = "urbanRail"
    METRO = "metro"
    WATER = "water"
    CABLEWAY = "cableway"
    FUNICULAR = "funicular"
    LIFT = "lift"
    SNOW_AND_ICE = "snowAndIce"
    TAXI = "taxi"
    SELF_DRIVE = "selfDrive"
    FOOT = "foot"
    BICYCLE = "bicycle"
    MOTORCYCLE = "motorcycle"
    CAR = "car"
    SHUTTLE = "shuttle"
