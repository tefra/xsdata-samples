from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingBayStatusEnumeration(StrEnum):
    AVAILABLE = "available"
    IN_USE = "inUse"
    OUT_OF_SERVICE = "outOfService"
    RESERVED = "reserved"
    UNKNOWN = "unknown"
