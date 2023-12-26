from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.airport_5 import Airport5
from travelport.models.city_5 import City5
from travelport.models.city_or_airport_5 import CityOrAirport5
from travelport.models.coordinate_location_5 import CoordinateLocation5
from travelport.models.distance_5 import Distance5
from travelport.models.rail_location_5 import RailLocation5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class TypeSearchLocation5:
    class Meta:
        name = "typeSearchLocation"

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
    coordinate_location: None | CoordinateLocation5 = field(
        default=None,
        metadata={
            "name": "CoordinateLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
        },
    )
    rail_location: None | RailLocation5 = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
        },
    )
    distance: None | Distance5 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v34_0",
        },
    )
