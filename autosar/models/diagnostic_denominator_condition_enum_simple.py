from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticDenominatorConditionEnumSimple(Enum):
    """
    :cvar VALUE_500_MILES: Condition based on definition of 500miles
        conditions as defined for OBD2.
    :cvar COLDSTART: Condition based on definition of "cold start" as
        defined for EU5+
    :cvar EVAP: Condition based on definition of "EVAP" conditions as
        defined for OBD2.
    :cvar INDIVIDUAL: condition based on definition of individual
        requirements.
    :cvar OBD: Condition based on definition of OBD requirements.
    """
    VALUE_500_MILES = "-500-MILES"
    COLDSTART = "COLDSTART"
    EVAP = "EVAP"
    INDIVIDUAL = "INDIVIDUAL"
    OBD = "OBD"
