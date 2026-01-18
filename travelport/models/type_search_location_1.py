from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.airport_1 import Airport1
from travelport.models.city_1 import City1
from travelport.models.city_or_airport_1 import CityOrAirport1
from travelport.models.coordinate_location_1 import CoordinateLocation1
from travelport.models.distance_1 import Distance1
from travelport.models.rail_location_1 import RailLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class TypeSearchLocation1:
    class Meta:
        name = "typeSearchLocation"

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
    coordinate_location: None | CoordinateLocation1 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    rail_location: None | RailLocation1 = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    distance: None | Distance1 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
