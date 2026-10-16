from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleOrientationEnumeration(StrEnum):
    FORWARDS = "forwards"
    BACKWARDS = "backwards"
    UNKNOWN = "unknown"
