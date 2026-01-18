from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SenderIntentEnumSimple(Enum):
    """
    :cvar WILL_SEND: The sender will send the event or field notifier.
    :cvar WONT_SEND: The sender won't send the event or field notifier.
    """

    WILL_SEND = "WILL-SEND"
    WONT_SEND = "WONT-SEND"
