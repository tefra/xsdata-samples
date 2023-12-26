from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagPduTypeSimple(Enum):
    """
    :cvar DIAG_REQUEST: Diagnostic Request
    :cvar DIAG_RESPONSE: Diagnostic Response
    """

    DIAG_REQUEST = "DIAG-REQUEST"
    DIAG_RESPONSE = "DIAG-RESPONSE"
