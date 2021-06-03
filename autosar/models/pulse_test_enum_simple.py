from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PulseTestEnumSimple(Enum):
    """
    :cvar DISABLE: Disables the pulse test
    :cvar ENABLE: Enables the pulse test
    """
    DISABLE = "DISABLE"
    ENABLE = "ENABLE"
