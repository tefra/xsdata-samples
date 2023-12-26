from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticCompareTypeEnumSimple(Enum):
    """
    :cvar IS_EQUAL: equal
    :cvar IS_GREATER_OR_EQUAL: greater than or equal
    :cvar IS_GREATER_THAN: greater than
    :cvar IS_LESS_OR_EQUAL: less than or equal
    :cvar IS_LESS_THAN: less than
    :cvar IS_NOT_EQUAL: not equal
    """

    IS_EQUAL = "IS-EQUAL"
    IS_GREATER_OR_EQUAL = "IS-GREATER-OR-EQUAL"
    IS_GREATER_THAN = "IS-GREATER-THAN"
    IS_LESS_OR_EQUAL = "IS-LESS-OR-EQUAL"
    IS_LESS_THAN = "IS-LESS-THAN"
    IS_NOT_EQUAL = "IS-NOT-EQUAL"
