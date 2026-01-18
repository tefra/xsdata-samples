from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CanTpChannelModeTypeSimple(Enum):
    """
    :cvar FULL_DUPLEX_MODE: full duplex channel mode
    :cvar HALF_DUPLEX_MODE: half duplex channel mode
    """

    FULL_DUPLEX_MODE = "FULL-DUPLEX-MODE"
    HALF_DUPLEX_MODE = "HALF-DUPLEX-MODE"
