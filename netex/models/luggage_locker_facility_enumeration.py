from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageLockerFacilityEnumeration(StrEnum):
    OTHER = "other"
    LOCKERS = "lockers"
    OVERSIZE_LOCKERS = "oversizeLockers"
    LEFT_LUGGAGE_COUNTER = "leftLuggageCounter"
    BIKE_RACK = "bikeRack"
    CLOAKROOM = "cloakroom"
