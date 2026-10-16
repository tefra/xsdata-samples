from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ScopingMethodEnumeration(StrEnum):
    EXPLICIT_STOPS = "explicitStops"
    IMPLICIT_SPATIAL_PROJECTION = "implicitSpatialProjection"
    EXPLICIT_PERIPHERY_STOPS = "explicitPeripheryStops"
    OTHER = "other"
