from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TimeSynchronizationKindEnumSimple(Enum):
    """
    :cvar OFFSET: Defines that the requested time base shall be an
        offset time based.
    :cvar SYNCHRONIZED: Defines that the requested time base shall be a
        synchronized time based.
    """
    OFFSET = "OFFSET"
    SYNCHRONIZED = "SYNCHRONIZED"
