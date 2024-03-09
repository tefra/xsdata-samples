from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeVehicleLocation(Enum):
    """
    The type of location requested, such as resort, city center.
    """

    TERMINAL = "Terminal"
    SHUTTLE_ON_AIRPORT = "ShuttleOnAirport"
    SHUTTLE_OFF_AIRPORT = "ShuttleOffAirport"
    RAILWAY_STATION = "RailwayStation"
    HOTEL = "Hotel"
    CAR_DEALER = "CarDealer"
    CITY_CENTER_DOWNTOWN = "CityCenterDowntown"
    EAST_OF_CITY_CENTER = "EastOfCityCenter"
    SOUTH_OF_CITY_CENTER = "SouthOfCityCenter"
    WEST_OF_CITY_CENTER = "WestOfCityCenter"
    NORTH_OF_CITY_CENTER = "NorthOfCityCenter"
    PORT_OR_FERRY = "PortOrFerry"
    NEAR_RESORT = "NearResort"
    AIRPORT = "Airport"
    UNKNOWN = "Unknown"
