from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NecessaryForceEnumeration(StrEnum):
    NO_FORCE = "noForce"
    LIGHT_FORCE = "lightForce"
    MEDIUM_FORCE = "mediumForce"
    HEAVY_FORCE = "heavyForce"
    UNKNOWN = "unknown"
