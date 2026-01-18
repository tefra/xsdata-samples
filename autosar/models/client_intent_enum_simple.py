from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ClientIntentEnumSimple(Enum):
    """
    :cvar WILL_CALL: The client will call this method.
    :cvar WONT_CALL: The client won't call this method.
    """

    WILL_CALL = "WILL-CALL"
    WONT_CALL = "WONT-CALL"
