from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VehicleType2Enum(Enum):
    """
    Vehicle types which are currently not supported in vehicleType.

    :cvar MOTORHOME: Motorhome
    :cvar LIGHT_GOODS_VEHICLE: Light goods vehicle
    :cvar HEAVY_GOODS_VEHICLE: Heavy goods vehicle
    :cvar MINIBUS: Minibus
    :cvar SMALL_CAR: Small car
    :cvar LARGE_CAR: Large car
    :cvar LIGHT_GOODS_VEHICLE_WITH_TRAILER: Light goods vehicle with
        trailer
    :cvar HEAVY_GOODS_VEHICLE_WITH_TRAILER: Heavy goods vehicle with
        trailer
    :cvar HEAVY_HAULAGE_VEHICLE: Heavy-haulage vehicle
    :cvar PASSENGER_CAR: Passenger car
    :cvar UNKNOWN: Unknown.
    """
    MOTORHOME = "motorhome"
    LIGHT_GOODS_VEHICLE = "lightGoodsVehicle"
    HEAVY_GOODS_VEHICLE = "heavyGoodsVehicle"
    MINIBUS = "minibus"
    SMALL_CAR = "smallCar"
    LARGE_CAR = "largeCar"
    LIGHT_GOODS_VEHICLE_WITH_TRAILER = "lightGoodsVehicleWithTrailer"
    HEAVY_GOODS_VEHICLE_WITH_TRAILER = "heavyGoodsVehicleWithTrailer"
    HEAVY_HAULAGE_VEHICLE = "heavyHaulageVehicle"
    PASSENGER_CAR = "passengerCar"
    UNKNOWN = "unknown"
