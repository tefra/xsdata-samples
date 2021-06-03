from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RptExecutionControlEnumSimple(Enum):
    """
    :cvar CONDITIONAL: The ExecutableEntity is only executed when the
        rapid prototyping disable flag is NOT set.
    :cvar NONE_VALUE: The ExecutableEntity is executed without specific
        rapid prototyping condition.
    """
    CONDITIONAL = "CONDITIONAL"
    NONE_VALUE = "NONE"
