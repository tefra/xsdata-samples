from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeSupplierType2(Enum):
    """
    The category of supplier that may apply. (Air, Car, Hotel, etc).
    """

    AIR = "Air"
    VEHICLE = "Vehicle"
    HOTEL = "Hotel"
    RAIL = "Rail"
    OTHER = "Other"
