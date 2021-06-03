from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SoftwareClusterDependencyLogicalOperatorEnumSimple(Enum):
    """
    :cvar LOGICAL_AND: logical and
    :cvar LOGICAL_OR: logical or
    """
    LOGICAL_AND = "LOGICAL-AND"
    LOGICAL_OR = "LOGICAL-OR"
