from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


class ReferenceDataSearchItemType(StrEnum):
    AIRPORT = "Airport"
    CARRIER = "Carrier"
    CITY = "City"
    COUNTRY = "Country"
    CURRENCY = "Currency"
    EQUIPMENT = "Equipment"
    PASSENGER_TYPE = "PassengerType"
    SSR_TYPE = "SsrType"
    STATE = "State"
