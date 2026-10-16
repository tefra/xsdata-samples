from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PduCollectionTriggerEnumSimple(StrEnum):
    """
    :cvar ALWAYS: Pdu will trigger the transmission of the data.
    :cvar NEVER: Pdu will be buffered and will not trigger the
        transmission of the data.
    """

    ALWAYS = "ALWAYS"
    NEVER = "NEVER"
