from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LockerTypeEnumeration(StrEnum):
    LEFT_LUGGAGE_OFFICE = "leftLuggageOffice"
    LOCKERS = "lockers"
    OVERSIZE_LOCKERS = "oversizeLockers"
    BIKE_RACK = "bikeRack"
    BIKE_CARRIAGE = "bikeCarriage"
    OTHER = "other"
