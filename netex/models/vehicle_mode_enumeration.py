from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleModeEnumeration(Enum):
    AIR = "air"
    BUS = "bus"
    COACH = "coach"
    FERRY = "ferry"
    METRO = "metro"
    RAIL = "rail"
    TROLLEY_BUS = "trolleyBus"
    TRAM = "tram"
    WATER = "water"
    CABLEWAY = "cableway"
    FUNICULAR = "funicular"
    LIFT = "lift"
    SNOW_AND_ICE = "snowAndIce"
    OTHER = "other"
