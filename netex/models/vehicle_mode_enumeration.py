from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleModeEnumeration(StrEnum):
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
