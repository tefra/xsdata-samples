from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_3 import Airport3
from travelport.models.city_3 import City3
from travelport.models.city_or_airport_3 import CityOrAirport3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class TypeLocation3:
    class Meta:
        name = "typeLocation"

    airport: None | Airport3 = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
    city: None | City3 = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
    city_or_airport: None | CityOrAirport3 = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
