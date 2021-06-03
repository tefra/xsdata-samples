from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SendIndicationEnumSimple(Enum):
    """
    :cvar ANY_SEND_OPERATION: This value represents the requirement that
        any send operation of the Software Cluster is indicated.
    :cvar NONE_VALUE: This value represents the requirement that send
        operations of the Software Cluster are not indicated.
    """
    ANY_SEND_OPERATION = "ANY-SEND-OPERATION"
    NONE_VALUE = "NONE"
