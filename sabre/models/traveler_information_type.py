from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.air_traveler_type import AirTravelerType
from sabre.models.passenger_type_quantity_type import PassengerTypeQuantityType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TravelerInformationType:
    """
    Specifies passenger numbers and types.

    Attributes:
        passenger_type_quantity: Specifies number of passengers using
            Passenger Type Codes.
        air_traveler: Information profiling the person traveling Gender
            - the gender of the customer, if needed BirthDate - Date of
            Birth Currency - the preferred currency in which monetary
            amounts should be returned.
    """

    passenger_type_quantity: list[PassengerTypeQuantityType] = field(
        default_factory=list,
        metadata={
            "name": "PassengerTypeQuantity",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )
    air_traveler: None | AirTravelerType = field(
        default=None,
        metadata={
            "name": "AirTraveler",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
