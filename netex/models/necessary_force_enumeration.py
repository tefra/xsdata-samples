from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NecessaryForceEnumeration(Enum):
    NO_FORCE = "noForce"
    LIGHT_FORCE = "lightForce"
    MEDIUM_FORCE = "mediumForce"
    HEAVY_FORCE = "heavyForce"
    UNKNOWN = "unknown"
