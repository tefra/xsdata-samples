from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class EquipmentOrSystemFaultTypeEnum(Enum):
    """
    Types of fault, malfunctioning or non operational conditions of equipment or
    systems.

    :cvar NOT_WORKING: Not working or functioning.
    :cvar OUT_OF_SERVICE: Out of service (usually for operational
        reasons).
    :cvar WORKING_INCORRECTLY: Working incorrectly.
    :cvar WORKING_INTERMITTENTLY: Working intermittently.
    """
    NOT_WORKING = "notWorking"
    OUT_OF_SERVICE = "outOfService"
    WORKING_INCORRECTLY = "workingIncorrectly"
    WORKING_INTERMITTENTLY = "workingIntermittently"
