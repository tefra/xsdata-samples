from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ServerArgumentImplPolicyEnumSimple(Enum):
    """
    :cvar USE_ARGUMENT_TYPE: The argument type of the RunnableEntity is
        derived from the AutosarDataType of the ArgumentPrototype.
    :cvar USE_ARRAY_BASE_TYPE: The argument type of the RunnableEntity
        is derived from the AutosarDataType of the elements of the array
        that corresponds to the ArgumentPrototype. This represents the
        base type of the array in C.
    :cvar USE_VOID: The argument type of the RunnableEntity is void.
    """

    USE_ARGUMENT_TYPE = "USE-ARGUMENT-TYPE"
    USE_ARRAY_BASE_TYPE = "USE-ARRAY-BASE-TYPE"
    USE_VOID = "USE-VOID"
