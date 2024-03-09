from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_2 import Airport2
from travelport.models.city_2 import City2
from travelport.models.city_or_airport_2 import CityOrAirport2
from travelport.models.coordinate_location_2 import CoordinateLocation2
from travelport.models.distance_2 import Distance2
from travelport.models.rail_location_2 import RailLocation2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TypeSearchLocation2:
    class Meta:
        name = "typeSearchLocation"

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
    coordinate_location: None | CoordinateLocation2 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    rail_location: None | RailLocation2 = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
    distance: None | Distance2 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        },
    )
