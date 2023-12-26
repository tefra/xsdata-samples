from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class UdpCollectionTriggerEnumSimple(Enum):
    """
    :cvar ALWAYS: ServiceInterface element will trigger the transmission
        of the data.
    :cvar NEVER: ServiceInterface element will be buffered and will not
        trigger the transmission of the data.
    """

    ALWAYS = "ALWAYS"
    NEVER = "NEVER"
