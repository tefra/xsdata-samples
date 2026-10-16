from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


class TypeOtherPreference1(StrEnum):
    """
    Specify the OtherPreference. (ie.

    Cruise, Taxi, etc).
    """

    CRUISE = "Cruise"
    FERRY = "Ferry"
    LIMO = "Limo"
    TAXI = "Taxi"
    TOUR = "Tour"
