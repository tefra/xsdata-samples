from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RequestTypeEnumSimple(Enum):
    """
    :cvar FUNCTIONAL: This enum literal defines a FUNCTIONAL
        DiagnosticMessage request.
    :cvar PHYSICAL: This enum literal defines a PHYSICAL
        DiagnosticMessage request.
    """

    FUNCTIONAL = "FUNCTIONAL"
    PHYSICAL = "PHYSICAL"
