from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeAreaInfo(Enum):
    """
    The type of area category, such as AirportMain, AirportSecondary.
    """
    AIRPORT_MAIN = "AirportMain"
    AIRPORT_SECONDARY = "AirportSecondary"
    CITY_CENTER_DOWNTOWN = "CityCenterDowntown"
    EAST_OF_CITY_CENTER = "EastOfCityCenter"
    SOUTH_OF_CITY_CENTER = "SouthOfCityCenter"
    WEST_OF_CITY_CENTER = "WestOfCityCenter"
    NORTH_OF_CITY_CENTER = "NorthOfCityCenter"
    PORT_OR_FERRY = "PortOrFerry"
    NEAR_RESORT = "NearResort"
    RAILWAY_STATION = "RailwayStation"
