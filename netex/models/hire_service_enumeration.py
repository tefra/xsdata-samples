from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class HireServiceEnumeration(Enum):
    SCOOTER_HIRE = "scooterHire"
    CYCLE_HIRE = "cycleHire"
    MOTORCYCLE_HIRE = "motorcycleHire"
    CAR_HIRE = "carHire"
    VEHICLE_HIRE = "vehicleHire"
    BOAT_HIRE = "boatHire"
    RECREATIONAL_DEVICE_HIRE = "recreationalDeviceHire"
