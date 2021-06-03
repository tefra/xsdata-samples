from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SwServiceReentranceEnumSimple(Enum):
    """
    :cvar REENTRANCE: If this element is not defined the service cannot
        be invoked when it is executing.
    """
    REENTRANCE = "REENTRANCE"
