from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_5 import Airport5
from travelport.models.city_5 import City5
from travelport.models.city_or_airport_5 import CityOrAirport5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeLocation5:
    class Meta:
        name = "typeLocation"

    airport: None | Airport5 = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
        },
    )
    city: None | City5 = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
        },
    )
    city_or_airport: None | CityOrAirport5 = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
        },
    )
