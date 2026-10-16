from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class DataTypeType(StrEnum):
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
