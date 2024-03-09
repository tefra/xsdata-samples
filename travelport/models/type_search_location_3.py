from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_3 import Airport3
from travelport.models.city_3 import City3
from travelport.models.city_or_airport_3 import CityOrAirport3
from travelport.models.coordinate_location_3 import CoordinateLocation3
from travelport.models.distance_3 import Distance3
from travelport.models.rail_location_3 import RailLocation3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class TypeSearchLocation3:
    class Meta:
        name = "typeSearchLocation"

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
    coordinate_location: None | CoordinateLocation3 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
    rail_location: None | RailLocation3 = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
    distance: None | Distance3 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        },
    )
