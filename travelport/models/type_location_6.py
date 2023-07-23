from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.airport_6 import Airport6
from travelport.models.city_6 import City6
from travelport.models.city_or_airport_6 import CityOrAirport6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypeLocation6:
    class Meta:
        name = "typeLocation"

    airport: None | Airport6 = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    city: None | City6 = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
    city_or_airport: None | CityOrAirport6 = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        }
    )
