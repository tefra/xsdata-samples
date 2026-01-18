from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CppImplementationDataTypeSubtypesEnum(Enum):
    CPP_IMPLEMENTATION_DATA_TYPE = "CPP-IMPLEMENTATION-DATA-TYPE"
    CUSTOM_CPP_IMPLEMENTATION_DATA_TYPE = "CUSTOM-CPP-IMPLEMENTATION-DATA-TYPE"
    STD_CPP_IMPLEMENTATION_DATA_TYPE = "STD-CPP-IMPLEMENTATION-DATA-TYPE"
