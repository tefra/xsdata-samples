from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TiltTypeEnumeration(Enum):
    STRONG_LEFT_TILT = "strongLeftTilt"
    MEDIUM_LEFT_TILT = "mediumLeftTilt"
    NEARLY_FLAT = "nearlyFlat"
    MEDIUM_RIGHT_TILT = "mediumRightTilt"
    STRONG_RIGHT_TILT = "strongRightTilt"
    UNKNOWN = "unknown"
