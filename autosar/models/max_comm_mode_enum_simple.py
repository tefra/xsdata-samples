from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class MaxCommModeEnumSimple(Enum):
    """
    :cvar FULL: Full communication is requested.
    :cvar NONE_VALUE: No communication is requested.
    :cvar SILENT: Silent communication is requested: Only listening but
        not "talking".
    """
    FULL = "FULL"
    NONE_VALUE = "NONE"
    SILENT = "SILENT"
