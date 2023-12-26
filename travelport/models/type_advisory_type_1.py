from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeAdvisoryType1(Enum):
    """
    Specify the type of Advisory.
    """

    AGENCY = "Agency"
    AIR = "Air"
    CUSTOMER = "Customer"
    DATES = "Dates"
    HOTELS = "Hotels"
    MARKET_RELATED = "Market Related"
    PASSPORT = "Passport"
    PROMOTIONS = "Promotions"
    SEASONAL = "Seasonal"
    SPECIALS = "Specials"
    SUPPLIER = "Supplier"
    TRAVEL = "Travel"
    VEHICLE = "Vehicle"
    VISA = "Visa"
