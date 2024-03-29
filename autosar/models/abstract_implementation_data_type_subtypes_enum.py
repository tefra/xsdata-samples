from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AbstractImplementationDataTypeSubtypesEnum(Enum):
    ABSTRACT_IMPLEMENTATION_DATA_TYPE = "ABSTRACT-IMPLEMENTATION-DATA-TYPE"
    CPP_IMPLEMENTATION_DATA_TYPE = "CPP-IMPLEMENTATION-DATA-TYPE"
    CUSTOM_CPP_IMPLEMENTATION_DATA_TYPE = "CUSTOM-CPP-IMPLEMENTATION-DATA-TYPE"
    IMPLEMENTATION_DATA_TYPE = "IMPLEMENTATION-DATA-TYPE"
    STD_CPP_IMPLEMENTATION_DATA_TYPE = "STD-CPP-IMPLEMENTATION-DATA-TYPE"
