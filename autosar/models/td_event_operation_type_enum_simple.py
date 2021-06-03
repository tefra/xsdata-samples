from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventOperationTypeEnumSimple(Enum):
    """
    :cvar OPERATION_CALL_RECEIVED: A point in time where the call of the
        referenced operation is received by the server SWC.
    :cvar OPERATION_CALL_RESPONSE_RECEIVED: A point in time where the
        client SWC has received the response of the referenced operation
        call.
    :cvar OPERATION_CALL_RESPONSE_SENT: A point in time where the server
        SWC has terminated with the execution of the referenced
        operation, and has sent out a response.
    :cvar OPERATION_CALLED: A point in time where the referenced
        operation is called by the client SWC.
    """
    OPERATION_CALL_RECEIVED = "OPERATION-CALL-RECEIVED"
    OPERATION_CALL_RESPONSE_RECEIVED = "OPERATION-CALL-RESPONSE-RECEIVED"
    OPERATION_CALL_RESPONSE_SENT = "OPERATION-CALL-RESPONSE-SENT"
    OPERATION_CALLED = "OPERATION-CALLED"
