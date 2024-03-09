from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_6 import Airport6
from travelport.models.city_6 import City6
from travelport.models.city_or_airport_6 import CityOrAirport6
from travelport.models.coordinate_location_6 import CoordinateLocation6
from travelport.models.distance_6 import Distance6
from travelport.models.rail_location_6 import RailLocation6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class TypeSearchLocation6:
    class Meta:
        name = "typeSearchLocation"

    airport: None | Airport6 = field(
        default=None,
        metadata={
            "name": "Airport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        },
    )
    city: None | City6 = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        },
    )
    city_or_airport: None | CityOrAirport6 = field(
        default=None,
        metadata={
            "name": "CityOrAirport",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        },
    )
    coordinate_location: None | CoordinateLocation6 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        },
    )
    rail_location: None | RailLocation6 = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        },
    )
    distance: None | Distance6 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v38_0",
        },
    )
