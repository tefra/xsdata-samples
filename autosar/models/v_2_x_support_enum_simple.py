from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class V2XSupportEnumSimple(Enum):
    """
    :cvar V_2_X_ACTIVE_SUPPORTED: This means that the EcuInstance
        supports V2X communication as both the sender and the receiver
        of communication.
    :cvar V_2_X_NOT_SUPPORTED: This EcuInstance does not support V2X
        communication
    """
    V_2_X_ACTIVE_SUPPORTED = "V-2-X-ACTIVE-SUPPORTED"
    V_2_X_NOT_SUPPORTED = "V-2-X-NOT-SUPPORTED"
