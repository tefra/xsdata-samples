from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventServiceInstanceEventTypeEnumSimple(Enum):
    """
    :cvar ADAPTIVE_EVENT_RECEIVED: A point in time where an event
        required by a service subscriber is received through the service
        port of the service subscriber.
    :cvar ADAPTIVE_EVENT_SENT: A point in time where an event provided
        by a service is sent through the service port of the service
        provider.
    """
    ADAPTIVE_EVENT_RECEIVED = "ADAPTIVE-EVENT-RECEIVED"
    ADAPTIVE_EVENT_SENT = "ADAPTIVE-EVENT-SENT"
