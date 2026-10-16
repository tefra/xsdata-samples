from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RampTurningSpacePositionEnumeration(StrEnum):
    NONE = "none"
    BOTTOM = "bottom"
    TOP = "top"
    TOP_AND_BOTTOM = "topAndBottom"
