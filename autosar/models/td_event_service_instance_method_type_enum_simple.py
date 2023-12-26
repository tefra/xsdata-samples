from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventServiceInstanceMethodTypeEnumSimple(Enum):
    """
    :cvar ADAPTIVE_METHOD_CALL_RECEIVED: A point in time where a method
        call of a service is received through the service provider's
        service port.
    :cvar ADAPTIVE_METHOD_CALLED: A point in time where a method of a
        service is called through the service subscriber's service port.
    :cvar ADAPTIVE_METHOD_RESPONSE_RECEIVED: A point in time where a
        response of a method call of a service is received through the
        service subscribers's service port.
    :cvar ADAPTIVE_METHOD_RESPONSE_SENT: A point in time where a
        response of a method call of a service is sent through the
        service provider's service port.
    """

    ADAPTIVE_METHOD_CALL_RECEIVED = "ADAPTIVE-METHOD-CALL-RECEIVED"
    ADAPTIVE_METHOD_CALLED = "ADAPTIVE-METHOD-CALLED"
    ADAPTIVE_METHOD_RESPONSE_RECEIVED = "ADAPTIVE-METHOD-RESPONSE-RECEIVED"
    ADAPTIVE_METHOD_RESPONSE_SENT = "ADAPTIVE-METHOD-RESPONSE-SENT"
