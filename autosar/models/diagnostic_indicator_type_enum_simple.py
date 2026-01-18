from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticIndicatorTypeEnumSimple(Enum):
    """
    :cvar AMBER_WARNING: Amber Warning Lamp
    :cvar MALFUNCTION: Malfunction Indicator Lamp
    :cvar PROTECT_LAMP: Protect Lamp
    :cvar RED_STOP_LAMP: Red Stop Lamp
    :cvar WARNING: Warning
    """

    AMBER_WARNING = "AMBER-WARNING"
    MALFUNCTION = "MALFUNCTION"
    PROTECT_LAMP = "PROTECT-LAMP"
    RED_STOP_LAMP = "RED-STOP-LAMP"
    WARNING = "WARNING"
