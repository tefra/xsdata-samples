from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ContainerIPduHeaderTypeEnumSimple(Enum):
    """
    :cvar LONG_HEADER: Header size is 64 bit: * Header Id 32 bit * Dlc
        32 bit
    :cvar NO_HEADER: No Header is used and the location of each
        containedPdu in the ContainerPdu is statically configured.
    :cvar SHORT_HEADER: Header size is 32 bit: * Header Id 24 bit * Dlc
        8 bit.
    """
    LONG_HEADER = "LONG-HEADER"
    NO_HEADER = "NO-HEADER"
    SHORT_HEADER = "SHORT-HEADER"
