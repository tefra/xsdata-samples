from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessModeEnumeration(StrEnum):
    FOOT = "foot"
    BICYCLE = "bicycle"
    BOAT = "boat"
    CAR = "car"
    TAXI = "taxi"
    SHUTTLE = "shuttle"
    SKI = "ski"
    SKATE = "skate"
    MOTORCYCLE = "motorcycle"
    SCOOTER = "scooter"
