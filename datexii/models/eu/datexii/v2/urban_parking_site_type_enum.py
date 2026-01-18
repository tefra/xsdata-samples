from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class UrbanParkingSiteTypeEnum(Enum):
    """
    The type of an urban parking site.

    :cvar ON_STREET_PARKING: Vehicles are parking on the roadside.
    :cvar OFF_STREET_PARKING: Vehicles are parking off the road, e.g. on
        a parking space, a car park or some other area designed for
        parking.
    :cvar OTHER: The parking is associated with some other location.
    """

    ON_STREET_PARKING = "onStreetParking"
    OFF_STREET_PARKING = "offStreetParking"
    OTHER = "other"
