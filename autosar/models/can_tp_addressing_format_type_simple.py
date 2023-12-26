from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CanTpAddressingFormatTypeSimple(Enum):
    """
    :cvar EXTENDED: To use extended addressing format.
    :cvar MIXED: To use mixed 11bit addressing format.
    :cvar MIXED_29_BIT: To use mixed 29bit addressing format
    :cvar NORMALFIXED: To use normal fixed addressing format
    :cvar STANDARD: To use normal addressing format.
    """

    EXTENDED = "EXTENDED"
    MIXED = "MIXED"
    MIXED_29_BIT = "MIXED-29-BIT"
    NORMALFIXED = "NORMALFIXED"
    STANDARD = "STANDARD"
