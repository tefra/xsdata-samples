from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ApiPrincipleEnumSimple(Enum):
    """
    :cvar COMMON: The Rte or SchM API is provided for the whole software
        component / BSW Module
    :cvar PER_EXECUTABLE: The Rte or SchM API is provided for a specific
        ExecutableEntity of a software component / BSW Module
    """

    COMMON = "COMMON"
    PER_EXECUTABLE = "PER-EXECUTABLE"
