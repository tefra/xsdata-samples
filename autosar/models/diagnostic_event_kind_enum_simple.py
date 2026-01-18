from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticEventKindEnumSimple(Enum):
    """
    :cvar BSW: The event is assigned to a BSW module.
    :cvar SWC: The event is assigned to a SWC.
    """

    BSW = "BSW"
    SWC = "SWC"
