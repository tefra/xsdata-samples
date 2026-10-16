from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TiltTypeEnumeration(StrEnum):
    STRONG_LEFT_TILT = "strongLeftTilt"
    MEDIUM_LEFT_TILT = "mediumLeftTilt"
    NEARLY_FLAT = "nearlyFlat"
    MEDIUM_RIGHT_TILT = "mediumRightTilt"
    STRONG_RIGHT_TILT = "strongRightTilt"
    UNKNOWN = "unknown"
