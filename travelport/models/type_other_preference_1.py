from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeOtherPreference1(Enum):
    """Specify the OtherPreference.

    (ie. Cruise, Taxi, etc)
    """
    CRUISE = "Cruise"
    FERRY = "Ferry"
    LIMO = "Limo"
    TAXI = "Taxi"
    TOUR = "Tour"
