from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class DataTypeType(Enum):
    """
    Enumerates C argument data types.
    """

    INT = "int"
    UNSIGNED_INT = "unsigned int"
    LONG = "long"
    UNSIGNED_LONG = "unsigned long"
    FLOAT = "float"
    DOUBLE = "double"
    CHAR = "char *"
    VOID = "void *"
