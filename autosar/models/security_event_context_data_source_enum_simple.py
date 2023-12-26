from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SecurityEventContextDataSourceEnumSimple(Enum):
    """
    :cvar USE_FIRST_CONTEXT_DATA: Context data of first received
        security event shall be used for resulting qualified security
        event.
    :cvar USE_LAST_CONTEXT_DATA: Context data of last received security
        event shall be used for resulting qualified security event.
    """

    USE_FIRST_CONTEXT_DATA = "USE-FIRST-CONTEXT-DATA"
    USE_LAST_CONTEXT_DATA = "USE-LAST-CONTEXT-DATA"
