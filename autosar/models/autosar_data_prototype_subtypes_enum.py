from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AutosarDataPrototypeSubtypesEnum(Enum):
    ARGUMENT_DATA_PROTOTYPE = "ARGUMENT-DATA-PROTOTYPE"
    AUTOSAR_DATA_PROTOTYPE = "AUTOSAR-DATA-PROTOTYPE"
    FIELD_VALUE = "FIELD"
    PARAMETER_DATA_PROTOTYPE = "PARAMETER-DATA-PROTOTYPE"
    PERSISTENCY_DATA_ELEMENT = "PERSISTENCY-DATA-ELEMENT"
    VARIABLE_DATA_PROTOTYPE = "VARIABLE-DATA-PROTOTYPE"