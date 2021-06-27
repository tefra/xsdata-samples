from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ArgumentDirectionEnumSimple(Enum):
    """
    :cvar IN: The argument value is passed to the callee.
    :cvar INOUT: The argument value is passed to the callee but also
        passed back from the callee to the caller.
    :cvar OUT: The argument value is passed from the callee  to the
        caller.
    """
    IN = "IN"
    INOUT = "INOUT"
    OUT = "OUT"
