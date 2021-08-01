from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RequestTypeEnum(Enum):
    """
    Types of requests that may be made by a client on a supplier.

    :cvar CATALOGUE: A request for the supplier's catalogue.
    :cvar FILTER: A request for the client's filter as currently stored
        by the supplier.
    :cvar REQUEST_DATA: A request for current data.
    :cvar REQUEST_HISTORICAL_DATA: A request for historical data, i.e.
        data which was valid within an historical time window.
    :cvar SUBSCRIPTION: A request for a client's subscription as
        currently held by a supplier.
    """
    CATALOGUE = "catalogue"
    FILTER = "filter"
    REQUEST_DATA = "requestData"
    REQUEST_HISTORICAL_DATA = "requestHistoricalData"
    SUBSCRIPTION = "subscription"
