from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


class RateMatchIndicatorStatus(Enum):
    """
    Properties
    ----------
    AVAILABLE
        Number of items requested for the IndicatorType is available
    NOT_AVAILABLE
        Number of items requested for the IndicatorType is not available.
        The actual number available is provided against Value
    SUBSTITUTE_OFFERED
        A substitute has been offered for the originally requested number
        and/or type. The substituted available is provided in against Value
    MAXIMUM_EXCEEDED
        Number of items requested for the IndicatorType exceeds the maximum
        applicable value. The substituted available is provided in against
        Value
    """

    AVAILABLE = "Available"
    NOT_AVAILABLE = "NotAvailable"
    SUBSTITUTE_OFFERED = "SubstituteOffered"
    MAXIMUM_EXCEEDED = "MaximumExceeded"
