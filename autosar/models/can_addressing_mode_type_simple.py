from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CanAddressingModeTypeSimple(Enum):
    """
    :cvar EXTENDED: Extended 29-bit-identifiers are used (CAN 2.0B)
    :cvar STANDARD: Standard 11-bit-identifiers are used (CAN 2.0A)
    """

    EXTENDED = "EXTENDED"
    STANDARD = "STANDARD"
