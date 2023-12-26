from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnumSimple(Enum):
    """
    :cvar CLEAR_DYNAMICALLY_DEFINE_DATA_IDENTIFIER: Clear the specified
        dynamic data identifier.
    :cvar DEFINE_BY_IDENTIFIER: The definition of dynamic data
        identifier shall be done via a reference to a diagnostic data
        identifier.
    :cvar DEFINE_BY_MEMORY_ADDRESS: The definition of dynamic data
        identifier shall be done via a reference to a memory address.
    """

    CLEAR_DYNAMICALLY_DEFINE_DATA_IDENTIFIER = (
        "CLEAR-DYNAMICALLY-DEFINE-DATA-IDENTIFIER"
    )
    DEFINE_BY_IDENTIFIER = "DEFINE-BY-IDENTIFIER"
    DEFINE_BY_MEMORY_ADDRESS = "DEFINE-BY-MEMORY-ADDRESS"
