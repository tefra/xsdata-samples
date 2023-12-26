from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeVehicleCategory(Enum):
    """
    The category of vehicle.
    """

    CAR = "Car"
    VAN = "Van"
    SUV = "SUV"
    CONVERTIBLE = "Convertible"
    TRUCK = "Truck"
    STATION_WAGON = "StationWagon"
    PICKUP = "Pickup"
    ALL_TERRAIN = "AllTerrain"
    RECREATIONAL = "Recreational"
    SPORT = "Sport"
    SPECIAL = "Special"
    EXTENDED_CAB_PICKUP = "ExtendedCabPickup"
    REGULAR_CAB_PICKUP = "RegularCabPickup"
    SPECIAL_OFFER = "SpecialOffer"
    COUPE = "Coupe"
    MONOSPACE = "Monospace"
    ROADSTER = "Roadster"
    CROSSOVER = "Crossover"
    MOTORCYCLE = "Motorcycle"
    LIMO = "Limo"
    MOTORHOME = "Motorhome"
    TWO_WHEEL_VEHICLE = "TwoWheelVehicle"
    COMMERCIAL_VAN_OR_TRUCK = "CommercialVanOrTruck"
