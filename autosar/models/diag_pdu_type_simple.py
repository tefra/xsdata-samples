from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagPduTypeSimple(StrEnum):
    """
    :cvar DIAG_REQUEST: Diagnostic Request
    :cvar DIAG_RESPONSE: Diagnostic Response
    """

    DIAG_REQUEST = "DIAG-REQUEST"
    DIAG_RESPONSE = "DIAG-RESPONSE"
