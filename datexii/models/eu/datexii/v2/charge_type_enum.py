from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ChargeTypeEnum(Enum):
    """
    Charge type.

    :cvar MINIMUM: Minimum price for the given interval.
    :cvar MAXIMUM: Maximum price for the given interval.
    :cvar ADDITIONAL_INTERVAL_PRICE: Price for all intervals following
        the first interval.
    :cvar SEASON_TICKET: Season ticket.
    :cvar TEMPORARY_PRICE: Temporary price.
    :cvar FIRST_INTERVAL_PRICE: Price for the first interval, e.g. the
        first hour. See also 'additional'.
    :cvar FREE_PARKING: Free Parking. Set charge to 0.
    :cvar FLAT: Flat fee.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """

    MINIMUM = "minimum"
    MAXIMUM = "maximum"
    ADDITIONAL_INTERVAL_PRICE = "additionalIntervalPrice"
    SEASON_TICKET = "seasonTicket"
    TEMPORARY_PRICE = "temporaryPrice"
    FIRST_INTERVAL_PRICE = "firstIntervalPrice"
    FREE_PARKING = "freeParking"
    FLAT = "flat"
    UNKNOWN = "unknown"
    OTHER = "other"
