from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_1 import Airport1
from travelport.models.city_1 import City1
from travelport.models.city_or_airport_1 import CityOrAirport1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeLocation1:
    class Meta:
        name = "typeLocation"

    airport: None | Airport1 = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    city: None | City1 = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    city_or_airport: None | CityOrAirport1 = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
