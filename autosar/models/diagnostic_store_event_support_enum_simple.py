from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticStoreEventSupportEnumSimple(Enum):
    """
    :cvar ALL: The server supports both, storing and not storing the
        event.
    :cvar NO_STORE_EVENT: The event terminates when the server is
        powered down.
    :cvar STORE_EVENT: The event is persisted over a power down cycle.
    """

    ALL = "ALL"
    NO_STORE_EVENT = "NO-STORE-EVENT"
    STORE_EVENT = "STORE-EVENT"
