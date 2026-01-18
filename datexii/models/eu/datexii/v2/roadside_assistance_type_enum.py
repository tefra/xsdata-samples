from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RoadsideAssistanceTypeEnum(Enum):
    """
    Types of road side assistance.

    :cvar AIR_AMBULANCE: Air ambulance assistance.
    :cvar BUS_PASSENGER_ASSISTANCE: Bus passenger assistance.
    :cvar EMERGENCY_SERVICES: Emergency services assistance.
    :cvar FIRST_AID: First aid assistance.
    :cvar FOOD_DELIVERY: Food delivery.
    :cvar HELICOPTER_RESCUE: Helicopter rescue.
    :cvar VEHICLE_REPAIR: Vehicle repair assistance.
    :cvar VEHICLE_RECOVERY: Vehicle recovery.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    AIR_AMBULANCE = "airAmbulance"
    BUS_PASSENGER_ASSISTANCE = "busPassengerAssistance"
    EMERGENCY_SERVICES = "emergencyServices"
    FIRST_AID = "firstAid"
    FOOD_DELIVERY = "foodDelivery"
    HELICOPTER_RESCUE = "helicopterRescue"
    VEHICLE_REPAIR = "vehicleRepair"
    VEHICLE_RECOVERY = "vehicleRecovery"
    OTHER = "other"
