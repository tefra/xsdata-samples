from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypePrivateFare(Enum):
    """List the types of private fares, Agency private fare, Airline private Fare
    and Unknown.

    Also, this enumaration list includes PrivateFare to indetify private
    fares for GDSs where we can not identify specific private fares.
    """
    UNKNOWN_TYPE = "UnknownType"
    PRIVATE_FARE = "PrivateFare"
    AGENCY_PRIVATE_FARE = "AgencyPrivateFare"
    AIRLINE_PRIVATE_FARE = "AirlinePrivateFare"
