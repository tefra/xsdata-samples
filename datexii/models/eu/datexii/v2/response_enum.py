from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ResponseEnum(Enum):
    """
    Types of response that a supplier can return to a requesting client.

    :cvar ACKNOWLEDGE: An acknowledgement that the supplier has received
        and complied with the client's request.
    :cvar CATALOGUE_REQUEST_DENIED: A notification that the supplier has
        denied the client's request for a catalogue.
    :cvar FILTER_REQUEST_DENIED: A notification that the supplier has
        denied the client's request for a filter.
    :cvar REQUEST_DENIED: A notification that the supplier has denied
        the client's request for a data.
    :cvar SUBSCRIPTION_REQUEST_DENIED: A notification that the supplier
        has denied the client's request for a subscription.
    """
    ACKNOWLEDGE = "acknowledge"
    CATALOGUE_REQUEST_DENIED = "catalogueRequestDenied"
    FILTER_REQUEST_DENIED = "filterRequestDenied"
    REQUEST_DENIED = "requestDenied"
    SUBSCRIPTION_REQUEST_DENIED = "subscriptionRequestDenied"
