from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class SavedTripActivityType(StrEnum):
    LOW_FARE_SEARCH = "LowFareSearch"
    AIR_PRICE = "AirPrice"
    VEHICLE_SEARCH_AVAILABILITY = "VehicleSearchAvailability"
    VEHICLE_BOOK = "VehicleBook"
    HOTEL_DETAILS_SEARCH = "HotelDetailsSearch"
    HOTEL_RULES_SEARCH = "HotelRulesSearch"
    HOTEL_SEARCH = "HotelSearch"
