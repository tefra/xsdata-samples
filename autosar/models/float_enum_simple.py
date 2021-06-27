from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class FloatEnumSimple(Enum):
    """
    :cvar FLOAT: This indicates that a page formatter is allowed to
        float the table to optimize the pagination. This is for example
        supported by TeX.
    :cvar NO_FLOAT: This indicates that a page formatter is not allowed
        to float the object to optimize the pagination.
    """
    FLOAT = "FLOAT"
    NO_FLOAT = "NO-FLOAT"
