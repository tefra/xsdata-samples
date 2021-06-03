from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ArrayImplPolicyEnumSimple(Enum):
    """
    :cvar PAYLOAD_AS_ARRAY: This configuration demands the
        implementation of the payload as an array.
    :cvar PAYLOAD_AS_POINTER_TO_ARRAY: This configuration demands the
        implementation of the payload as a pointer to an array.
    """
    PAYLOAD_AS_ARRAY = "PAYLOAD-AS-ARRAY"
    PAYLOAD_AS_POINTER_TO_ARRAY = "PAYLOAD-AS-POINTER-TO-ARRAY"
