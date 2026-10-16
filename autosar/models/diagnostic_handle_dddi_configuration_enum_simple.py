from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticHandleDddiConfigurationEnumSimple(StrEnum):
    """
    :cvar NON_VOLATILE: This indicates that the configuration of
        DynamicallyDefineDataIdentifier shall be stored as non-volatile
        data.
    :cvar VOLATILE: This indicates that the configuration of
        DynamicallyDefineDataIdentifier shall be handled as volatile
        data.
    """

    NON_VOLATILE = "NON-VOLATILE"
    VOLATILE = "VOLATILE"
