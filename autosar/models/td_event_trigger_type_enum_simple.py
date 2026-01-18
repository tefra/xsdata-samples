from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventTriggerTypeEnumSimple(Enum):
    """
    :cvar TRIGGER_ACTIVATED: A point in time where the referenced
        trigger has been successfully released and is activating
        runnable entities of the receiving SW-C.
    :cvar TRIGGER_RELEASED: A point in time where the referenced trigger
        has been successfully released by the emitting SW-C.
    """

    TRIGGER_ACTIVATED = "TRIGGER-ACTIVATED"
    TRIGGER_RELEASED = "TRIGGER-RELEASED"
