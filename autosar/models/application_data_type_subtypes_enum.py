from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ApplicationDataTypeSubtypesEnum(Enum):
    APPLICATION_ARRAY_DATA_TYPE = "APPLICATION-ARRAY-DATA-TYPE"
    APPLICATION_ASSOC_MAP_DATA_TYPE = "APPLICATION-ASSOC-MAP-DATA-TYPE"
    APPLICATION_COMPOSITE_DATA_TYPE = "APPLICATION-COMPOSITE-DATA-TYPE"
    APPLICATION_DATA_TYPE = "APPLICATION-DATA-TYPE"
    APPLICATION_DEFERRED_DATA_TYPE = "APPLICATION-DEFERRED-DATA-TYPE"
    APPLICATION_PRIMITIVE_DATA_TYPE = "APPLICATION-PRIMITIVE-DATA-TYPE"
    APPLICATION_RECORD_DATA_TYPE = "APPLICATION-RECORD-DATA-TYPE"