from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ReceiverIntentEnumSimple(Enum):
    """
    :cvar WILL_RECEIVE: The receiver will receive the event or field
        notifier.
    :cvar WONT_RECEIVE: The receiver won't receive the event or field
        notifier.
    """

    WILL_RECEIVE = "WILL-RECEIVE"
    WONT_RECEIVE = "WONT-RECEIVE"
