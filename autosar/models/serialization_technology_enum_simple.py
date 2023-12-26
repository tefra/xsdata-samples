from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SerializationTechnologyEnumSimple(Enum):
    """
    :cvar SIGNAL_BASED: Signal-Based serializer.
    :cvar SOMEIP: SOME/IP Serializer
    """

    SIGNAL_BASED = "SIGNAL-BASED"
    SOMEIP = "SOMEIP"
