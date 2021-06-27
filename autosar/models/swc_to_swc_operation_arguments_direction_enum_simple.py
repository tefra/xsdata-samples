from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SwcToSwcOperationArgumentsDirectionEnumSimple(Enum):
    """
    :cvar IN: IN (all IN and INOUT arguments)
    :cvar OUT: OUT (all OUT and INOUT arguments) .
    """
    IN = "IN"
    OUT = "OUT"
