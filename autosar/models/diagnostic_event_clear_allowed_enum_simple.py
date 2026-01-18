from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticEventClearAllowedEnumSimple(Enum):
    """
    :cvar ALWAYS: The clearing is allowed unconditionally.
    :cvar NEVER: The clearing is never allowed.
    :cvar REQUIRES_CALLBACK_EXECUTION: In case the clearing of a
        Diagnostic Event has to be allowed or prohibited through the SWC
        interface CallbackClearEventAllowed, the SWC has to indicate
        this by defining appropriate ServiceNeeds (i.e.
        DiagnosticEventNeeds).
    """

    ALWAYS = "ALWAYS"
    NEVER = "NEVER"
    REQUIRES_CALLBACK_EXECUTION = "REQUIRES-CALLBACK-EXECUTION"
