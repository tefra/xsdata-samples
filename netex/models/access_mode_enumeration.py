from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AccessModeEnumeration(Enum):
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
