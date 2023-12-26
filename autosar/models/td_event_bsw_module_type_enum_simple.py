from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventBswModuleTypeEnumSimple(Enum):
    """
    :cvar BSW_M_ENTRY_CALL_RETURNED: A point in time where the call of
        the associated BswModuleEntry has returned.
    :cvar BSW_M_ENTRY_CALLED: A point in time where the associated
        BswModuleEntry has been called.
    """

    BSW_M_ENTRY_CALL_RETURNED = "BSW-M-ENTRY-CALL-RETURNED"
    BSW_M_ENTRY_CALLED = "BSW-M-ENTRY-CALLED"
