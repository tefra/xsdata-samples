from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticInitialEventStatusEnumSimple(Enum):
    """
    :cvar RETURN_ON_EVENT_CLEARED: This means that the ResponseOnEvent
        is initially cleared.
    :cvar RETURN_ON_EVENT_STOPPED: This means that the ResponseOnEvent
        is initially stopped.
    """

    RETURN_ON_EVENT_CLEARED = "RETURN-ON-EVENT-CLEARED"
    RETURN_ON_EVENT_STOPPED = "RETURN-ON-EVENT-STOPPED"
