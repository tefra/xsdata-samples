from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataLimitKindEnumSimple(Enum):
    """
    :cvar MAX: Limitation to maximum value
    :cvar MIN: Limitation to minimum value
    :cvar NONE_VALUE: No limitation applicable
    """
    MAX = "MAX"
    MIN = "MIN"
    NONE_VALUE = "NONE"
