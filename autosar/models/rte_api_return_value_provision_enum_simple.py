from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class RteApiReturnValueProvisionEnumSimple(Enum):
    """
    :cvar NO_RETURN_VALUE_PROVIDED: The RTE API shall not provide a
        return value.
    :cvar RETURN_VALUE_PROVIDED: The RTE API shall provide a return
        value.
    """
    NO_RETURN_VALUE_PROVIDED = "NO-RETURN-VALUE-PROVIDED"
    RETURN_VALUE_PROVIDED = "RETURN-VALUE-PROVIDED"
