from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFaresIndicator(Enum):
    """
    Defines the type of fares to return (Only public fares, Only private fares,
    Only agency private fares, Only airline private fares or all fares)

    Properties
    ----------
    PUBLIC_FARES_ONLY
    PRIVATE_FARES_ONLY
    AGENCY_PRIVATE_FARES_ONLY
    AIRLINE_PRIVATE_FARES_ONLY
    PUBLIC_AND_PRIVATE_FARES
    NET_FARES_ONLY
    ALL_FARES
        Applicable for 1G/1V air shop only
    """

    PUBLIC_FARES_ONLY = "PublicFaresOnly"
    PRIVATE_FARES_ONLY = "PrivateFaresOnly"
    AGENCY_PRIVATE_FARES_ONLY = "AgencyPrivateFaresOnly"
    AIRLINE_PRIVATE_FARES_ONLY = "AirlinePrivateFaresOnly"
    PUBLIC_AND_PRIVATE_FARES = "PublicAndPrivateFares"
    NET_FARES_ONLY = "NetFaresOnly"
    ALL_FARES = "AllFares"
