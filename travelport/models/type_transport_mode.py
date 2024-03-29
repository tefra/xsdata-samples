from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class TypeTransportMode(Enum):
    """
    Enumeration of all Train Transport Modes.
    """

    BICYCLE = "Bicycle"
    BOAT = "Boat"
    BUS = "Bus"
    CABLE_CAR = "Cable Car"
    CAR = "Car"
    CARRIAGE = "Carriage"
    COURTESY_CAR = "Courtesy car"
    HELICOPTER = "Helicopter"
    LIMOUSINE = "Limousine"
    METRO = "Metro"
    MONORAIL = "Monorail"
    MOTORBIKE = "Motorbike"
    PACK_ANIMAL = "Pack Animal"
    PLANE = "Plane"
    RENTAL_CAR = "Rental Car"
    RICKSHAW = "Rickshaw"
    SHUTTLE = "Shuttle"
    SUBWAY = "Subway"
    SEDAN_CHAIR = "Sedan Chair"
    TAXI = "Taxi"
    TRAIN = "Train"
    TROLLEY = "Trolley"
    TUBE = "Tube"
    WALK = "Walk"
    WATER_TAXI = "Water Taxi"
    OTHER = "Other"
    CAR_RUSH_HOUR = "Car/Rush hour"
    TAXI_RUSH_HOUR = "Taxi/Rush hour"
    NO_TRANSPORTATION = "No Transportation"
    EXPRESS_TRAIN = "Express Train"
    PUBLIC = "Public"
    SHIP_FERRY = "Ship/Ferry"
    UNDERGROUND = "Underground"
    TRAM_LIGHT_RAIL = "Tram/light rail"
    SHARED_TAXI = "Shared Taxi"
