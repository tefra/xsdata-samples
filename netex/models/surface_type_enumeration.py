from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SurfaceTypeEnumeration(Enum):
    ASPHALT = "asphalt"
    BRICKS = "bricks"
    COBBLES = "cobbles"
    EARTH = "earth"
    GRASS = "grass"
    LOOSE_SURFACE = "looseSurface"
    PAVING_STONES = "pavingStones"
    ROUGH_SURFACE = "roughSurface"
    SMOOTH = "smooth"
    OTHER = "other"
