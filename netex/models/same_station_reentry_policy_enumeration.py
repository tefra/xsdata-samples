from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameStationReentryPolicyEnumeration(StrEnum):
    BLOCKED = "blocked"
    NEW_FARE = "newFare"
    MAXIMUM_FARE = "maximumFare"
    ALLOWED = "allowed"
