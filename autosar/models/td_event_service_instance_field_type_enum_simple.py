from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventServiceInstanceFieldTypeEnumSimple(Enum):
    """
    :cvar ADAPTIVE_FIELD_GETTER_CALLED: A point in time where a field
        getter of a service is called by a service subscriber through
        the service port of the service subscriber.
    :cvar ADAPTIVE_FIELD_GETTER_COMPLETED: A point in time where a field
        getter of a service is completed and the result of the field
        getter is received through the service subscriber's service
        port.
    :cvar ADAPTIVE_FIELD_NOTIFICATION_RECEIVED: A point in time where a
        field notification required by a service subscriber is received
        through the service port of the service subscriber.
    :cvar ADAPTIVE_FIELD_NOTIFICATION_SENT: A point in time where a
        field notification provided by a service is sent through the
        service port of the service provider.
    :cvar ADAPTIVE_FIELD_SETTER_CALLED: A point in time where a field
        setter of a service is called by a service subscriber through
        the service port of the service subscriber.
    :cvar ADAPTIVE_FIELD_SETTER_COMPLETED: A point in time where a field
        setter of a service is completed and the result of the field
        setter is received through the service subscriber's service
        port.
    """
    ADAPTIVE_FIELD_GETTER_CALLED = "ADAPTIVE-FIELD-GETTER-CALLED"
    ADAPTIVE_FIELD_GETTER_COMPLETED = "ADAPTIVE-FIELD-GETTER-COMPLETED"
    ADAPTIVE_FIELD_NOTIFICATION_RECEIVED = "ADAPTIVE-FIELD-NOTIFICATION-RECEIVED"
    ADAPTIVE_FIELD_NOTIFICATION_SENT = "ADAPTIVE-FIELD-NOTIFICATION-SENT"
    ADAPTIVE_FIELD_SETTER_CALLED = "ADAPTIVE-FIELD-SETTER-CALLED"
    ADAPTIVE_FIELD_SETTER_COMPLETED = "ADAPTIVE-FIELD-SETTER-COMPLETED"
