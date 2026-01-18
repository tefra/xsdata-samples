from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_2 import Airport2
from travelport.models.city_2 import City2
from travelport.models.city_or_airport_2 import CityOrAirport2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class TypeLocation2:
    class Meta:
        name = "typeLocation"

    airport: None | Airport2 = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    city: None | City2 = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    city_or_airport: None | CityOrAirport2 = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
