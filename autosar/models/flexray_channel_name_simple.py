from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class FlexrayChannelNameSimple(StrEnum):
    """
    :cvar CHANNEL_A: Channel A
    :cvar CHANNEL_B: Channel B
    """

    CHANNEL_A = "CHANNEL-A"
    CHANNEL_B = "CHANNEL-B"
