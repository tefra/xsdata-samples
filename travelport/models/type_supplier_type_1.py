from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeSupplierType1(StrEnum):
    """
    The category of supplier that may apply. (Air, Car, Hotel, etc).
    """

    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    OTHER = "Other"
