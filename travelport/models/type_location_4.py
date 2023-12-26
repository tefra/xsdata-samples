from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.airport_4 import Airport4
from travelport.models.city_4 import City4
from travelport.models.city_or_airport_4 import CityOrAirport4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class TypeLocation4:
    class Meta:
        name = "typeLocation"

    airport: None | Airport4 = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    city: None | City4 = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    city_or_airport: None | CityOrAirport4 = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
