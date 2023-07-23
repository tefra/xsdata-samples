from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeOtherPreference2(Enum):
    """Specify the OtherPreference.

    (ie. Cruise, Taxi, etc)
    """
    CRUISE = "Cruise"
    FERRY = "Ferry"
    LIMO = "Limo"
    TAXI = "Taxi"
    TOUR = "Tour"
