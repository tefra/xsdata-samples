from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeAdvisoryType2(Enum):
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
