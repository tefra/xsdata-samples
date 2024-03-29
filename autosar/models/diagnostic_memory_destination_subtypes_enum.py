from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticMemoryDestinationSubtypesEnum(Enum):
    DIAGNOSTIC_MEMORY_DESTINATION = "DIAGNOSTIC-MEMORY-DESTINATION"
    DIAGNOSTIC_MEMORY_DESTINATION_MIRROR = (
        "DIAGNOSTIC-MEMORY-DESTINATION-MIRROR"
    )
    DIAGNOSTIC_MEMORY_DESTINATION_PRIMARY = (
        "DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY"
    )
    DIAGNOSTIC_MEMORY_DESTINATION_USER_DEFINED = (
        "DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED"
    )
