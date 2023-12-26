from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoftwareClusterDependencyOperatorEnumSimple(Enum):
    """
    :cvar IS_EQUAL: equal
    :cvar IS_GREATER_THAN: greater than
    :cvar IS_GREATER_THAN_OR_EQUAL: greater than or equal
    :cvar IS_LESS_THAN: less than
    :cvar IS_LESS_THAN_OR_EQUAL: less than or equal
    """

    IS_EQUAL = "IS-EQUAL"
    IS_GREATER_THAN = "IS-GREATER-THAN"
    IS_GREATER_THAN_OR_EQUAL = "IS-GREATER-THAN-OR-EQUAL"
    IS_LESS_THAN = "IS-LESS-THAN"
    IS_LESS_THAN_OR_EQUAL = "IS-LESS-THAN-OR-EQUAL"
