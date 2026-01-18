from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RentalPenaltyPolicyTypeEnumeration(Enum):
    REFUELLING = "refuelling"
    VEHICLE_TRANSFER = "vehicleTransfer"
    LATE_VEHICLE_RETURN = "lateVehicleReturn"
    NO_VEHICLE_RETURN = "noVehicleReturn"
    DAMAGE_TO_VEHICLE = "damageToVehicle"
    DAMAGE_TO_EQUIPMENT = "damageToEquipment"
    LOSS_OF_EQUIPMENT = "lossOfEquipment"
    ZONE_TRANSGRESSION = "zoneTransgression"
    TRAFFIC_FINE = "trafficFine"
    HANDLING_FEE_FOR_FINE = "handlingFeeForFine"
    OTHER = "other"
