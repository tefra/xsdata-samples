from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class HireFacilityEnumeration(StrEnum):
    UNKNOWN = "unknown"
    SCOOTER_HIRE = "scooterHire"
    VEHICLE_HIRE = "vehicleHire"
    CAR_HIRE = "carHire"
    MOTOR_CYCLE_HIRE = "motorCycleHire"
    CYCLE_HIRE = "cycleHire"
    TAXI = "taxi"
    BOAT_HIRE = "boatHire"
    RECREATION_DEVICE_HIRE = "recreationDeviceHire"
    OTHER = "other"
