from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AbstractAccessPointSubtypesEnum(Enum):
    ABSTRACT_ACCESS_POINT = "ABSTRACT-ACCESS-POINT"
    ASYNCHRONOUS_SERVER_CALL_POINT = "ASYNCHRONOUS-SERVER-CALL-POINT"
    ASYNCHRONOUS_SERVER_CALL_RESULT_POINT = "ASYNCHRONOUS-SERVER-CALL-RESULT-POINT"
    EXTERNAL_TRIGGERING_POINT_IDENT = "EXTERNAL-TRIGGERING-POINT-IDENT"
    INTERNAL_TRIGGERING_POINT = "INTERNAL-TRIGGERING-POINT"
    MODE_ACCESS_POINT_IDENT = "MODE-ACCESS-POINT-IDENT"
    MODE_SWITCH_POINT = "MODE-SWITCH-POINT"
    PARAMETER_ACCESS = "PARAMETER-ACCESS"
    SERVER_CALL_POINT = "SERVER-CALL-POINT"
    SYNCHRONOUS_SERVER_CALL_POINT = "SYNCHRONOUS-SERVER-CALL-POINT"
    VARIABLE_ACCESS = "VARIABLE-ACCESS"