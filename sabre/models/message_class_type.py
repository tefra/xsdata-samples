from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class MessageClassType(Enum):
    """
    Definies the available messaage class type.

    Attributes:
        E: Error
        W: Warrning
        D: Diagnostic
        I: Info
    """

    E = "E"
    W = "W"
    D = "D"
    I = "I"
