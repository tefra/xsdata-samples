from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class LinChecksumTypeSimple(Enum):
    """
    :cvar CLASSIC: Classic in communication with LIN 1.3 slave nodes
    :cvar ENHANCED: Enhanced in communication with LIN 2.0 slave nodes.
    """

    CLASSIC = "CLASSIC"
    ENHANCED = "ENHANCED"
