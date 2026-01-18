from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameStationReentryPolicyEnumeration(Enum):
    BLOCKED = "blocked"
    NEW_FARE = "newFare"
    MAXIMUM_FARE = "maximumFare"
    ALLOWED = "allowed"
