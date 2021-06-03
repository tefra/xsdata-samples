from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class HandleOutOfRangeStatusEnumSimple(Enum):
    """
    :cvar INDICATE: The RTE sets the return status to RTE_E_OUT_OF_RANGE
        if the received value is out of range and the attribute
        handleOutOfRange is not set to "none" or "invalid".
    :cvar SILENT: The RTE sets the return status to RTE_E_OK
    """
    INDICATE = "INDICATE"
    SILENT = "SILENT"
