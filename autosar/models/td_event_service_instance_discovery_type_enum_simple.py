from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TdEventServiceInstanceDiscoveryTypeEnumSimple(Enum):
    """
    :cvar ADAPTIVE_SERVICE_FIND_COMPLETED: A point in time where a
        service subscriber completes to find a needed service.
    :cvar ADAPTIVE_SERVICE_FIND_STARTED: A point in time where a service
        subscriber starts to find a needed service.
    :cvar ADAPTIVE_SERVICE_OFFER_COMPLETED: A point in time where a
        service provider completes to offer a needed service.
    :cvar ADAPTIVE_SERVICE_OFFER_STARTED: A point in time where a
        service provider starts to offer a needed service.
    :cvar ADAPTIVE_SERVICE_STOP_SUBSCRIPTION_COMPLETED: A point in time
        where a service subscriber completes to stop subscribing to a
        needed service.
    :cvar ADAPTIVE_SERVICE_STOP_SUBSCRIPTION_STARTED: A point in time
        where a service subscriber starts to stop subscribing to a
        needed service.
    :cvar ADAPTIVE_SERVICE_SUBSCRIPTION_ACKNOWLEDGE_COMPLETED: A point
        in time where a service provider completes to acknowledge
        subscription to a needed service.
    :cvar ADAPTIVE_SERVICE_SUBSCRIPTION_ACKNOWLEDGE_STARTED: A point in
        time where a service provider starts to acknowledge subscription
        to a needed service.
    :cvar ADAPTIVE_SERVICE_SUBSCRIPTION_COMPLETED: A point in time where
        a service subscriber completes to subscribe to a needed service.
    :cvar ADAPTIVE_SERVICE_SUBSCRIPTION_STARTED: A point in time where a
        service subscriber starts to subscribe to a needed service.
    """
    ADAPTIVE_SERVICE_FIND_COMPLETED = "ADAPTIVE-SERVICE-FIND-COMPLETED"
    ADAPTIVE_SERVICE_FIND_STARTED = "ADAPTIVE-SERVICE-FIND-STARTED"
    ADAPTIVE_SERVICE_OFFER_COMPLETED = "ADAPTIVE-SERVICE-OFFER-COMPLETED"
    ADAPTIVE_SERVICE_OFFER_STARTED = "ADAPTIVE-SERVICE-OFFER-STARTED"
    ADAPTIVE_SERVICE_STOP_SUBSCRIPTION_COMPLETED = "ADAPTIVE-SERVICE-STOP-SUBSCRIPTION-COMPLETED"
    ADAPTIVE_SERVICE_STOP_SUBSCRIPTION_STARTED = "ADAPTIVE-SERVICE-STOP-SUBSCRIPTION-STARTED"
    ADAPTIVE_SERVICE_SUBSCRIPTION_ACKNOWLEDGE_COMPLETED = "ADAPTIVE-SERVICE-SUBSCRIPTION-ACKNOWLEDGE-COMPLETED"
    ADAPTIVE_SERVICE_SUBSCRIPTION_ACKNOWLEDGE_STARTED = "ADAPTIVE-SERVICE-SUBSCRIPTION-ACKNOWLEDGE-STARTED"
    ADAPTIVE_SERVICE_SUBSCRIPTION_COMPLETED = "ADAPTIVE-SERVICE-SUBSCRIPTION-COMPLETED"
    ADAPTIVE_SERVICE_SUBSCRIPTION_STARTED = "ADAPTIVE-SERVICE-SUBSCRIPTION-STARTED"
