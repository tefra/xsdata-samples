from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MetroSubmodeEnumeration(StrEnum):
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    METRO = "metro"
    TUBE = "tube"
    URBAN_RAILWAY = "urbanRailway"
